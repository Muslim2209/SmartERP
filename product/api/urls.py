from django.urls import path

from product.views import products

app_name = 'api_product'

urlpatterns = [
    path('', products, name='product_list'),
]
