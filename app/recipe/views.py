from rest_framework import viewsets, mixins
from . import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from sys import path
from os.path import dirname as dir
from core.models import Tag


path.append(dir(path[0]))
__package__ = "core"


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')