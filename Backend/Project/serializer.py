from django.db.models import Q
from rest_framework import serializers

from Project.models import Project, Node, Graph, Edge
from Tree.models import Parameter


class NodeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Node.objects.create(**validated_data)

    class Meta:
        model = Node
        exclude = ['graph']


class EdgeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Edge.objects.create(**validated_data)

    class Meta:
        model = Edge
        exclude = ['graph']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "describe", "createdData", "updatedData")


class GraphSerializer(serializers.ModelSerializer):
    projectName = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    def get_projectName(self, obj):
        return Project.objects.all().filter(pk=obj.id).first().name

    def get_data(self, obj):
        res = dict()
        res["nodes"] = Node.objects.all().filter(graph=obj).values()
        for node in res["nodes"]:
            node["size"] = eval(node["size"])
            node["parameters"], node["outputs"], node["inputs"] = [], [], []
            Parameter.objects.all().filter(belongFunction__node__id=node["id"]).values()
            condition = Q(belongFunction__node__id=node["id"]) | Q(belongClass__node__id=node["id"])
            for parameter in Parameter.objects.all().filter(condition).values():
                if parameter["category"] == "parameter":
                    node["parameters"].append(parameter)
                elif parameter["category"] == "input":
                    node["inputs"].append(parameter)
                elif parameter["category"] == "output":
                    node["outputs"].append(parameter)
        res["edges"] = Edge.objects.all().filter(graph=obj).values()
        for edge in res["edges"]:
            attrs = ["end", "endPoint", "start", "startPoint"]
            for attr in attrs:
                edge[attr] = {
                    "x": eval(edge[attr])[0],
                    "y": eval(edge[attr])[1],
                }
        return res

    class Meta:
        model = Graph
        fields = ("project", "projectName", "data")
