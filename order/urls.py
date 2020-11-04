from django.urls import path

from order.views import order, create_order, update_order, delete_order

app_name = 'order'

urlpatterns = [
    path('', order, name='order_list'),
    path('<int:pk>/', update_order, name='order_detail'),
    path('add/<int:pk>/', create_order, name='create_order'),
    path('remove/<int:pk>/', delete_order, name='delete_order'),
]
