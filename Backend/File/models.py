from django.db import models


# Create your models here.
class DataSet(models.Model):
    name = models.CharField(max_length=255, verbose_name="数据集名")

    def __str__(self):
        return self.name


class File(models.Model):
    dataset = models.ForeignKey(to=DataSet, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to="file/", max_length=1024)

    class Meta:
        unique_together = ("dataset", "file")
