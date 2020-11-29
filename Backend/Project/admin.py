from django.contrib import admin

from Project.models import Project, Edge
from Project.models import Graph
from Project.models import Node


class NodeAdmin(admin.StackedInline):
    model = Node
    extra = 0


class EdgeAdmin(admin.StackedInline):
    model = Edge
    extra = 0


class GraphAdmin(admin.ModelAdmin):
    model = Graph
    inlines = [NodeAdmin, EdgeAdmin]


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("createdData", "updatedData")
    list_display = ("name", "describe", "createdData", "updatedData")


admin.site.register(Graph, GraphAdmin)
admin.site.register(Project, ProjectAdmin)
