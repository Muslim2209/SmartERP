from django.urls import path

from category.views import CategoryListView, CategoryUpdateView, CategoryAddView

app_name = 'category'

urlpatterns = [
    # path('', CategoryListView.as_view(), name='list'),
    # path('<str:item>/list/', CategoryListView.as_view(), name='list'),
    # path('<int:pk>/sub/', CategoryListView.as_view(), name='child_list'),
    # path('<int:pk>/', CategoryUpdateView.as_view(), name='edit'),
    # path('add/', CategoryAddView.as_view(), name='add'),
]
