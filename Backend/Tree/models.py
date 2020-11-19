from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Catalog(MPTTModel):
    name = models.CharField(max_length=255, verbose_name="目录名")
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Function(models.Model):
    functionName = models.CharField(max_length=255, verbose_name="函数名")
    name = models.CharField(max_length=255, verbose_name="昵称", default="", blank=True, null=True)
    describe = models.TextField(verbose_name="描述")

    belong = models.ForeignKey(to="Catalog", on_delete=models.PROTECT, null=True, blank=True, verbose_name="所属目录")

    def __str__(self):
        return self.name


class Class(models.Model):
    className = models.CharField(max_length=255, verbose_name="类名")
    name = models.CharField(max_length=255, verbose_name="昵称", default="", blank=True, null=True)
    describe = models.TextField(verbose_name="描述")

    belong = models.ForeignKey(to="Catalog", on_delete=models.PROTECT, null=True, blank=True, verbose_name="所属目录")

    def __str__(self):
        return self.name


class Parameter(models.Model):
    parameterName = models.CharField(max_length=255, verbose_name="参数名")
    name = models.CharField(max_length=255, verbose_name="昵称")
    describe = models.TextField(verbose_name="描述")
    type = models.CharField(max_length=255, verbose_name="类型", default="str")
    value = models.TextField(blank=True, null=True)
    belongClass = models.ForeignKey(to="Class", on_delete=models.PROTECT, null=True, blank=True)
    belongFunction = models.ForeignKey(to="Function", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name
