from .models import File
from .models import DataSet
from django.contrib import admin


class FileInline(admin.StackedInline):
    model = File
    extra = 1


class DataSetAdmin(admin.ModelAdmin):
    inlines = [FileInline]


# Register your models here.
admin.site.register(DataSet, DataSetAdmin)