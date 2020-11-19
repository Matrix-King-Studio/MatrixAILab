from django.db import models

from Project.models import Project


# Create your models here.
class DataSet(models.Model):
    name = models.CharField(max_length=255, verbose_name="数据集名")

    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class File(models.Model):
    dataset = models.ForeignKey(to=DataSet, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to="file/", max_length=1024)

    class Meta:
        unique_together = ("dataset", "file")
