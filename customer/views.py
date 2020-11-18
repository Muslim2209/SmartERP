from django.urls import reverse_lazy, resolve
from django.views.generic import ListView, CreateView, UpdateView

from customer.forms import CustomerForm, CustomerGroupForm
from customer.models import Customer, CustomerGroup


class CustomerGroupListView(ListView):
    model = CustomerGroup


class CustomerGroupAddView(CreateView):
    model = CustomerGroup
    form_class = CustomerGroupForm
    success_url = reverse_lazy('customer:group_list')


class CustomerGroupUpdateView(UpdateView):
    model = CustomerGroup
    form_class = CustomerGroupForm
    success_url = reverse_lazy('customer:group_list')


class CustomerListView(ListView):
    model = Customer


class CustomerAddView(CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer:list')


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer:list')
