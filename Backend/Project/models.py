import json

from django.db import models

from Tree.models import Function, Class


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name="项目名")
    describe = models.TextField(max_length=1024, blank=True, null=True, default="", verbose_name="项目描述")
    # TODO:添加 owner 作为项目所有人
    createdData = models.DateTimeField(auto_now_add=True, verbose_name="项目创建时间")
    updatedData = models.DateTimeField(auto_now_add=True, verbose_name="项目更新时间")

    def __str__(self):
        return self.name


class Graph(models.Model):
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.name


class Node(models.Model):
    id = models.CharField(max_length=50, verbose_name="节点id", primary_key=True)
    fontSize = models.IntegerField(verbose_name="节点名字体大小")
    label = models.CharField(max_length=50, verbose_name="节点名")
    size = models.CharField(max_length=50, verbose_name="节点尺寸")
    type = models.CharField(max_length=50, verbose_name="节点类型")
    shape = models.CharField(max_length=50, verbose_name="节点形状")
    x = models.IntegerField(verbose_name="节点x坐标")
    y = models.IntegerField(verbose_name="节点y坐标")
    valueType = models.CharField(max_length=50, verbose_name="节点运行结果类型", null=True, blank=True)
    value = models.TextField(verbose_name="节点运行结果", null=True, blank=True)

    graph = models.ForeignKey(to=Graph, on_delete=models.DO_NOTHING)
    classes = models.ForeignKey(to=Class, on_delete=models.DO_NOTHING, blank=True, null=True)
    function = models.ForeignKey(to=Function, on_delete=models.DO_NOTHING, blank=True, null=True)

    def setsize(self, size):
        self.size = json.dumps(size)

    def getsize(self):
        return json.loads(self.size)

    def setvalue(self, value):
        self.value = json.dumps(value)

    def getvalue(self):
        return json.loads(self.value)

    def __str__(self):
        return f"{self.id} - {self.label}"


class Edge(models.Model):
    id = models.CharField(max_length=50, verbose_name="节点id", primary_key=True)
    end = models.CharField(max_length=50)
    endPoint = models.CharField(max_length=50)
    endPointId = models.CharField(max_length=50)
    start = models.CharField(max_length=50)
    startPoint = models.CharField(max_length=50)
    startPointId = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    target = models.CharField(max_length=50)
    type = models.CharField(max_length=50, verbose_name="边类型")
    shape = models.CharField(max_length=50, verbose_name="边形状")

    graph = models.ForeignKey(to=Graph, on_delete=models.DO_NOTHING)
    sourceNode = models.ForeignKey(to=Node, on_delete=models.DO_NOTHING, related_name="sourceNode")
    targetNode = models.ForeignKey(to=Node, on_delete=models.DO_NOTHING, related_name="targetNode")

    def setend(self, end):
        self.end = json.dumps(end)

    def getend(self):
        return json.loads(self.end)

    def setstart(self, start):
        self.start = json.dumps(start)

    def getstart(self):
        return json.loads(self.start)

    def setendPoint(self, endPoint):
        self.endPoint = json.dumps(endPoint)

    def getendPoint(self):
        return json.loads(self.endPoint)

    def setstartPoint(self, startPoint):
        self.startPoint = json.dumps(startPoint)

    def getstartPoint(self):
        return json.loads(self.startPoint)

    def __str__(self):
        return f"{self.id}"
