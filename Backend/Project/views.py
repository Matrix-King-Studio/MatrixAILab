from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from File.models import DataSet
from File.serializers import DataSetSerializer
from Project.models import Project, Graph, Node, Edge
from Project.serializer import ProjectSerializer, GraphSerializer, NodeSerializer, EdgeSerializer


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
            serializer = DataSetSerializer(data=request.data)
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
