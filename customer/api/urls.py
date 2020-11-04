from django.urls import path

from customer.views import customer_list, customer_detail

app_name = 'api_customer'

urlpatterns = [
    path('', customer_list, name='customer_list'),
    path('<int:pk>/', customer_detail, name='customer_detail'),
]
