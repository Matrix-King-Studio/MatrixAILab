from rest_framework import serializers

from Tree.models import Catalog, Function, Class, Parameter


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'
