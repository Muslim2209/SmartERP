from django.urls import path, include
from rest_framework import routers

from product.api.views import ProductViewSet

app_name = 'api_product'

router = routers.DefaultRouter()

router.register('', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
