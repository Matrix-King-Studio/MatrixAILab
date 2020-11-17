from .models import Class
from .models import Function
from .models import Catalog
from .models import Parameter

from django.contrib import admin
from mptt.admin import MPTTModelAdmin


# Register your models here.
class ParameterInline(admin.StackedInline):
    model = Parameter
    extra = 1


class ClassAdmin(admin.ModelAdmin):
    inlines = [ParameterInline]


class FunctionAdmin(admin.ModelAdmin):
    inlines = [ParameterInline]


admin.site.register(Class, ClassAdmin)
admin.site.register(Function, FunctionAdmin)
admin.site.register(Catalog, MPTTModelAdmin)
