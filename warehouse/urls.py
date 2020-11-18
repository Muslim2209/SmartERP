from django.urls import path

from warehouse.views import WarehouseListView, WarehouseUpdateView, WarehouseAddView, WarehouseInputListView, \
    WarehouseInputUpdateView, WarehouseInputAddView, WarehouseRemainListView

app_name = 'warehouse'

urlpatterns = [
    path('', WarehouseListView.as_view(), name='list'),
    path('<int:pk>/', WarehouseUpdateView.as_view(), name='edit'),
    path('add/', WarehouseAddView.as_view(), name='add'),

    path('input/', WarehouseInputListView.as_view(), name='input_list'),
    path('input/<int:pk>/', WarehouseInputUpdateView.as_view(), name='input_edit'),
    path('input/add/', WarehouseInputAddView.as_view(), name='input_add'),

    path('remain/', WarehouseRemainListView.as_view(), name='remain'),
]
