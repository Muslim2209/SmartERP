from django.urls import path, include
from rest_framework.routers import DefaultRouter

from category.api.views import CategoryViewSet, GroupViewSet

router = DefaultRouter()

router.register('', CategoryViewSet, basename='category')
router.register('group', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
]
