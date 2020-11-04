from django.urls import path

from customer.views import customer_list, customer_detail, customer_add

app_name = 'customer'

urlpatterns = [
    path('', customer_list, name='list'),
    path('<int:pk>/', customer_detail, name='detail'),
    path('add/', customer_add, name='add'),
]
