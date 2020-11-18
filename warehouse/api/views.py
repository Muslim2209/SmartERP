from rest_framework import viewsets

from warehouse.api.serializers import WarehouseSerializer
from warehouse.models import Warehouse


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
