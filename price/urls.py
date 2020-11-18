from django.urls import path

from price.views import PriceListView, PriceAddView, PriceUpdateView, CurrencyListView, CurrencyAddView, \
    CurrencyUpdateView

app_name = 'price'

urlpatterns = [
    path('', PriceListView.as_view(), name='list'),
    path('add/', PriceAddView.as_view(), name='add'),
    path('<int:pk>/', PriceUpdateView.as_view(), name='edit'),

    path('currency/', CurrencyListView.as_view(), name='currency_list'),
    path('currency/add/', CurrencyAddView.as_view(), name='currency_add'),
    path('currency/<int:pk>/', CurrencyUpdateView.as_view(), name='currency_edit'),
]
