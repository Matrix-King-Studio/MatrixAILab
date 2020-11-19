from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name="项目名")
    describe = models.CharField(max_length=1024, blank=True, null=True, default="")
    # TODO:添加 owner 作为项目所有人
    createdData = models.DateTimeField(auto_now_add=True)
    updatedData = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
