from rest_framework import serializers
from sys import path
from os.path import dirname as dir
from core.models import Tag

path.append(dir(path[0]))
__package__ = "core"


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)
