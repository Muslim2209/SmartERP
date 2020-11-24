from django.urls import path

from unit.views import UnitListView, UnitAddView, UnitUpdateView, CaseListView, CaseAddView, CaseUpdateView

app_name = 'unit'

urlpatterns = [
    path('', UnitListView.as_view(), name='list'),
    path('add/', UnitAddView.as_view(), name='add'),
    path('<int:pk>/', UnitUpdateView.as_view(), name='edit'),

    path('box/', CaseListView.as_view(), name='case_list'),
    path('box/add/', CaseAddView.as_view(), name='case_add'),
    path('box/<int:pk>/', CaseUpdateView.as_view(), name='case_edit'),
]
