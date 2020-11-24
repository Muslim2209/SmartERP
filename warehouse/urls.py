from django.urls import path

from warehouse.views import *

app_name = 'warehouse'

urlpatterns = [
    path('', WarehouseListView.as_view(), name='list'),
    path('<int:pk>/', WarehouseUpdateView.as_view(), name='edit'),
    path('add/', WarehouseAddView.as_view(), name='add'),

    path('stock/', StockListView.as_view(), name='stock_list'),
    path('stock/<str:details>/', StockListView.as_view(), name='stock_list_details'),

    path('input/', ProductTransactionListView.as_view(), name='stock_input_list'),
    path('input/add/', ProductTransactionAddView.as_view(), name='stock_input_add'),
    path('input/<int:pk>/', ProductTransactionEditView.as_view(), name='stock_input_edit'),

    # path('input/', WarehouseInputListView.as_view(), name='input_list'),
    # path('input/<int:pk>/', WarehouseInputUpdateView.as_view(), name='input_edit'),
    # path('input/add/', WarehouseInputAddView.as_view(), name='input_add'),

    # path('balance/', WarehouseBalanceListView.as_view(), name='balance'),
]
