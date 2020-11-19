from django.forms import model_to_dict
from rest_framework import serializers

from File.models import File, DataSet


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("file", )


class DataSetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    file = serializers.SerializerMethodField()

    def get_file(self, obj):
        res = []
        for file in File.objects.all().filter(dataset=obj):
            tmp = {}
            file = model_to_dict(file)
            tmp["id"] = file["id"]
            tmp["dataset"] = file["dataset"]
            tmp["filePath"] = file["file"].url
            tmp["filename"] = file["file"].name.split("/")[-1]
            res.append(tmp)
        return res

    class Meta:
        model = DataSet
        fields = ("name", "project", "file")
