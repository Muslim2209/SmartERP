from django.db import transaction
from django.db.models import Sum
from django.urls import reverse_lazy, resolve
from django.views.generic import ListView, CreateView, UpdateView

from warehouse.forms import *
from warehouse.models import *


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


class StockListView(ListView):
    model = Stock

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        details = self.kwargs.get('details')
        context['details_url'] = resolve(self.request.path_info).url_name == 'stock_list_details'
        if details:
            context['stock_list'] = Stock.objects.values('product__name').annotate(quantity=Sum('quantity'),
                                                                                   product=F('product__name'),
                                                                                   warehouse=F('warehouse__name'))
        else:
            context['stock_list'] = Stock.objects.values('product__name').annotate(quantity=Sum('quantity'),
                                                                                   product=F('product__name'))
        return context


class ProductTransactionListView(ListView):
    model = ProductTransaction


class ProductTransactionAddView(CreateView):
    model = ProductTransaction
    fields = '__all__'
    # form_class = ProductTransactionFormset
    success_url = reverse_lazy('warehouse:stock_input_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['transactions'] = ProductTransactionFormset(self.request.POST)
        else:
            data['transactions'] = ProductTransactionFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        trans = context['transactions']
        with transaction.atomic():
            self.object = form.save()

            if trans.is_valid():
                trans.instance = self.object
                trans.save()
        return super().form_valid(form)


class ProductTransactionEditView(UpdateView):
    model = ProductTransaction
    fields = '__all__'
    # form_class = ProductTransactionForm
    success_url = reverse_lazy('warehouse:stock_input_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['transactions'] = ProductTransactionFormset(self.request.POST, instance=self.object)
        else:
            data['transactions'] = ProductTransactionFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        transactions = context['transactions']
        with transaction.atomic():
            self.object = form.save()

            if transactions.is_valid():
                transactions.instance = self.object
                transactions.save()
        return super().form_valid(form)

# class StockAddView(CreateView):
#     model = Stock
#     fields = '__all__'
#     success_url = reverse_lazy('warehouse:stock_list')
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         if self.request.POST:
#             data['inputs'] = StockFormSet(self.request.POST)
#         else:
#             data['inputs'] = StockFormSet()
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         inputs = context['inputs']
#         with transaction.atomic():
#             self.object = form.save()
#
#             if inputs.is_valid():
#                 inputs.instance = self.object
#                 inputs.save()
#         return super().form_valid(form)


# class StockUpdateView(CreateView):
#     model = Stock
#     form_class = StockForm
#     success_url = reverse_lazy('warehouse:stock_list')

# class WarehouseInputAddView(CreateView):
#     model = WarehouseInput
#     fields = '__all__'
#     success_url = reverse_lazy('warehouse:input_list')
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         if self.request.POST:
#             data['inputs'] = InputProductFormset(self.request.POST)
#         else:
#             data['inputs'] = InputProductFormset()
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         inputs = context['inputs']
#         with transaction.atomic():
#             self.object = form.save()
#
#             if inputs.is_valid():
#                 inputs.instance = self.object
#                 inputs.save()
#         return super().form_valid(form)
#
#
# class WarehouseInputUpdateView(UpdateView):
#     model = WarehouseInput
#     fields = '__all__'
#     success_url = reverse_lazy('warehouse:input_list')
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         if self.request.POST:
#             data['inputs'] = InputProductFormset(self.request.POST, instance=self.object)
#         else:
#             data['inputs'] = InputProductFormset(instance=self.object)
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         inputs = context['inputs']
#         with transaction.atomic():
#             self.object = form.save()
#
#             if inputs.is_valid():
#                 inputs.instance = self.object
#                 inputs.save()
#         return super().form_valid(form)
#
#
# class WarehouseBalanceListView(ListView):
#     model = Balance
#
#     def get_context_data(self, *args, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['balance_list'] = Balance.objects.all()
#         return context
