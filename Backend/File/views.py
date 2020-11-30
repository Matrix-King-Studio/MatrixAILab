import pandas as pd

from sklearn.impute import SimpleImputer

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from File.models import File
from File.serializers import FileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=True, methods=["GET"])
    def readFile(self, request, pk):
        file = self.queryset.filter(id=pk).values().first()
        df = pd.read_csv(f"./media/{file['file']}")
        self.cleanDataFrame(df)
        df = df.head(100)

        columns = []
        for item in df.columns.values:
            tmp = {
                "title": item,
                "dataIndex": item,
                "key": item,
            }

            if item == "Id":
                tmp["fixed"] = "left"
            columns.append(tmp)

        imp = SimpleImputer(strategy='most_frequent')
        df = imp.fit_transform(df)
        data = []
        for item in df:
            tmp = {"key": item[0]}
            for i in range(len(columns)):
                tmp[columns[i]["key"]] = item[i]
            data.append(tmp)

        return Response({
            "data": data,
            "columns": columns
        }, status=status.HTTP_200_OK)

    @staticmethod
    def cleanDataFrame(df, cutoff=0.5):
        for col in df.columns:
            n = len(df)
            cnt = df[col].count()
            if (float(cnt) / n) < cutoff:
                df.drop(col, axis=1, inplace=True)
