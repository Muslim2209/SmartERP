from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from product.forms import ProductForm, ProductGroupForm, ProductSubGroupForm
from product.models import Product, ProductGroup, ProductSubGroup


class ProductGroupListView(ListView):
    model = ProductGroup


class ProductGroupAddView(CreateView):
    model = ProductGroup
    form_class = ProductGroupForm
    success_url = reverse_lazy('product:group_list')


class ProductGroupUpdateView(UpdateView):
    model = ProductGroup
    form_class = ProductGroupForm
    success_url = reverse_lazy('product:group_list')


class ProductGroupDeleteView(DeleteView):
    model = ProductGroup
    success_url = reverse_lazy('product:group_list')


class ProductSubGroupListView(ListView):
    model = ProductSubGroup

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['subgroup_list'] = ProductSubGroup.objects.filter(group_id=self.kwargs.get('pk'))
        return context


class ProductSubGroupAddView(CreateView):
    model = ProductSubGroup
    form_class = ProductSubGroupForm
    success_url = reverse_lazy('product:group_sub_list')


class ProductSubGroupUpdateView(UpdateView):
    model = ProductSubGroup
    form_class = ProductSubGroupForm
    success_url = reverse_lazy('product:group_sub_list')


class ProductSubGroupDeleteView(DeleteView):
    model = ProductSubGroup
    success_url = reverse_lazy('product:group_sub_list')


class ProductListView(ListView):
    model = Product


class ProductAddView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:list')
