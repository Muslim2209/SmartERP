from django.urls import path

from product.views import ProductListView, ProductAddView, ProductUpdateView, \
    ProductGroupListView, ProductGroupAddView, ProductGroupUpdateView, ProductGroupDeleteView, \
    ProductSubGroupListView, ProductSubGroupAddView, ProductSubGroupUpdateView, ProductSubGroupDeleteView

app_name = 'product'

urlpatterns = [
    path('group/', ProductGroupListView.as_view(), name='group_list'),
    path('group/<int:pk>/', ProductGroupUpdateView.as_view(), name='group_edit'),
    path('group/<int:pk>/del/', ProductGroupDeleteView.as_view(), name='group_delete'),
    path('group/add/', ProductGroupAddView.as_view(), name='group_add'),

    path('group/<int:pk>/sub/', ProductSubGroupListView.as_view(), name='group_sub_list'),
    path('group/sub/<int:pk>/', ProductSubGroupUpdateView.as_view(), name='group_sub_edit'),
    path('group/sub/<int:pk>/del/', ProductSubGroupDeleteView.as_view(), name='group_sub_delete'),
    path('group/<int:pk>/sub/add/', ProductSubGroupAddView.as_view(), name='group_sub_add'),

    path('', ProductListView.as_view(), name='list'),
    path('<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('add/', ProductAddView.as_view(), name='add'),
]
