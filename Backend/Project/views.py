from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from File.models import DataSet
from File.serializers import DataSetSerializer
from Project.models import Project
from Project.serializer import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

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
