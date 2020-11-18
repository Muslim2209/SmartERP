from django.urls import path, include
from rest_framework import routers

from warehouse.api.views import WarehouseViewSet

router = routers.DefaultRouter()

router.register('', WarehouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
