from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from price.forms import PriceForm, CurrencyForm
from price.models import Price, Currency


class PriceListView(ListView):
    model = Price


class PriceAddView(CreateView):
    model = Price
    form_class = PriceForm
    success_url = reverse_lazy('price:list')


class PriceUpdateView(UpdateView):
    model = Price
    form_class = PriceForm
    success_url = reverse_lazy('price:list')


class CurrencyListView(ListView):
    model = Currency


class CurrencyAddView(CreateView):
    model = Currency
    form_class = CurrencyForm
    success_url = reverse_lazy('price:currency_list')


class CurrencyUpdateView(UpdateView):
    model = Currency
    form_class = CurrencyForm
    success_url = reverse_lazy('price:currency_list')
