from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from File.models import DataSet
from File.serializers import DataSetSerializer
from Project.models import Project, Graph, Node, Edge
from Project.serializer import ProjectSerializer, GraphSerializer, NodeSerializer, EdgeSerializer

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def trainTestSplit(X, y, test_size, random_state):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def readCsv(path, header):
    return pd.read_csv(filepath_or_buffer=path, header=header)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=["GET"])
    def graph(self, request, pk):
        if request.method == "GET":
            project = self.get_object()
            graph = Graph.objects.all().filter(project=project).first()
            serializer = GraphSerializer(graph)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["GET", "POST"])
    def dataSet(self, request, pk):
        if request.method == "GET":
            dataset = DataSet.objects.all().filter(project_id=pk).first()
            serializer = DataSetSerializer(dataset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == "POST":
            project = self.get_object()
            serializer = DataSetSerializer(data=request.trainData)
            serializer.is_valid(raise_exception=True)
            dataset = serializer.save()
            project.dataset_set = dataset
            project.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class GraphViewSet(viewsets.ModelViewSet):
    queryset = Graph.objects.all()
    serializer_class = GraphSerializer

    @action(methods=["GET", "POST", "DELETE", "PATCH"], detail=True)
    def data(self, request, pk):
        if request.method == "POST":
            nodes = request.data.get("nodes", None)
            edges = request.data.get("edges", None)
            for node in nodes:
                if not Node.objects.all().filter(id=node["id"]).exists():
                    nodeSerializer = NodeSerializer(data=node)
                    nodeSerializer.is_valid(raise_exception=True)
                    nodeSerializer.save(graph_id=pk)
            for edge in edges:
                if not Edge.objects.all().filter(id=edge["id"]).exists():
                    edge["sourceNode"] = edge["source"]
                    edge["targetNode"] = edge["target"]
                    edge["end"] = f"[{edge['end']['x']}, {edge['end']['y']}]"
                    edge["endPoint"] = f"[{edge['endPoint']['x']}, {edge['endPoint']['y']}]"
                    edge["start"] = f"[{edge['start']['x']}, {edge['start']['y']}]"
                    edge["startPoint"] = f"[{edge['startPoint']['x']}, {edge['startPoint']['y']}]"
                    edgeSerializer = EdgeSerializer(data=edge)
                    edgeSerializer.is_valid(raise_exception=True)
                    edgeSerializer.save(graph_id=pk)
            return Response({"message": "success!"}, status=status.HTTP_201_CREATED)

    @action(methods=["GET"], detail=True)
    def run(self, request, pk):
        # 读取训练数据集
        trainData = readCsv(r"G:\Project\MatrixAILab\Backend\media\file\train.csv", 0)

        trainData.drop("Id", axis=1, inplace=True)

        # 数据预处理
        na_count = trainData.isnull().sum().sort_values(ascending=False)
        na_rate = na_count / len(trainData)
        na_data = pd.concat([na_count, na_rate], axis=1, keys=['count', 'ratio'])
        trainData.drop(na_data[na_data['count'] > 1].index, axis=1, inplace=True)
        trainData.drop(trainData.loc[trainData['Electrical'].isnull()].index, inplace=True)
        for col in trainData.columns:
            if trainData[col].dtypes == "object":
                trainData[col], uniques = pd.factorize(trainData[col])

        # 训练/测试集划分
        XData, yData = trainData.iloc[:, :-1], trainData.iloc[:, -1]
        X_train, X_test, y_train, y_test = trainTestSplit(XData, yData, 0.33, 42)

        # 线性回归模型
        lr = LinearRegression()

        # 拟合
        lr.fit(X_train, y_train)

        # 评测
        score = lr.score(X_test, y_test)
        print(score)

        # 读取测试数据集
        testData = readCsv(r"G:\Project\MatrixAILab\Backend\media\file\test.csv", 0)

        # 数据预处理
        testID = testData["Id"]
        testData.drop("Id", axis=1, inplace=True)
        testData.drop(na_data[na_data['count'] > 1].index, axis=1, inplace=True)
        for col in testData.columns:
            if testData[col].dtypes == "object":
                testData[col], uniques = pd.factorize(testData[col])
            testData[col].fillna(testData[col].mean(), inplace=True)

        # 预测
        predict = lr.predict(testData)
        submit = pd.concat([testID, pd.Series(abs(predict))], axis=1, keys=["Id", "SalePrice"])
        submit.to_csv(r"G:\Project\MatrixAILab\Backend\media\file\submisson.csv", index=False)

        return Response({"message": "success!"}, status=status.HTTP_200_OK)

    @action(methods=["GET", "POST"], detail=True)
    def node(self, request, pk):
        if request.method == "GET":
            nodeId = request.GET.get("nodeId", None)
            node = Node.objects.all().filter(id=nodeId).first()
            data = {"type": node.valueType, "value": None}

            if node.valueType == "DataFrame":
                data["value"] = []
                df = pd.read_json(node.value)
                for item in df.values:
                    data["value"].append({"Id": item[0], "SalePrice": item[1]})
            else:
                data["value"] = node.value
            return Response(data, status=status.HTTP_200_OK)
