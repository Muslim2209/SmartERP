from django.urls import path

from customer.views import CustomerListView, CustomerAddView, CustomerUpdateView, \
    CustomerGroupListView, CustomerGroupAddView, CustomerGroupUpdateView

app_name = 'customer'

urlpatterns = [
    path('group/', CustomerGroupListView.as_view(), name='group_list'),
    path('group/<int:pk>/', CustomerGroupUpdateView.as_view(), name='group_edit'),
    path('group/add/', CustomerGroupAddView.as_view(), name='group_add'),

    path('', CustomerListView.as_view(), name='list'),
    path('<int:pk>/', CustomerUpdateView.as_view(), name='edit'),
    path('add/', CustomerAddView.as_view(), name='add'),
]
