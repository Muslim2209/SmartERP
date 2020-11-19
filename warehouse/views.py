from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from warehouse.forms import WarehouseForm, InputProductFormset
from warehouse.models import Warehouse, WarehouseInput, Balance


class WarehouseListView(ListView):
    model = Warehouse


class WarehouseAddView(CreateView):
    model = Warehouse
    form_class = WarehouseForm
    success_url = reverse_lazy('warehouse:list')


class WarehouseUpdateView(UpdateView):
    model = Warehouse
    form_class = WarehouseForm
    success_url = reverse_lazy('warehouse:list')


class WarehouseInputListView(ListView):
    model = WarehouseInput


class WarehouseInputAddView(CreateView):
    model = WarehouseInput
    fields = '__all__'
    success_url = reverse_lazy('warehouse:input_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['inputs'] = InputProductFormset(self.request.POST)
        else:
            data['inputs'] = InputProductFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        inputs = context['inputs']
        with transaction.atomic():
            self.object = form.save()

            if inputs.is_valid():
                inputs.instance = self.object
                inputs.save()
        return super().form_valid(form)


class WarehouseInputUpdateView(UpdateView):
    model = WarehouseInput
    fields = '__all__'
    success_url = reverse_lazy('warehouse:input_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['inputs'] = InputProductFormset(self.request.POST, instance=self.object)
        else:
            data['inputs'] = InputProductFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        inputs = context['inputs']
        with transaction.atomic():
            self.object = form.save()

            if inputs.is_valid():
                inputs.instance = self.object
                inputs.save()
        return super().form_valid(form)


class WarehouseBalanceListView(ListView):
    model = Balance

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['balance_list'] = Balance.objects.all()
        return context
