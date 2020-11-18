from django.urls import path, include
from rest_framework import routers

from customer.api.views import CustomerViewSet

app_name = 'api_customer'

router = routers.DefaultRouter()

router.register('', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
