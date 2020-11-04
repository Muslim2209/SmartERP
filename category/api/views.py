from rest_framework import viewsets

from category.api.serializers import CategorySerializer, GroupSerializer
from category.models import Category, Group


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
