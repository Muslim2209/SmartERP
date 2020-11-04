from django.urls import path

from product.views import products, product_add

app_name = 'product'

urlpatterns = [
    path('', products, name='list'),
    path('add/', product_add, name='add'),
]
