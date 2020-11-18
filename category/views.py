from django.shortcuts import render
from django.urls import resolve, reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView

from category.forms import CategoryForm
from category.models import Category, SubCategory


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.kwargs.get('item')
        print('item:\n', item)
        if item:
            context['category_list'] = Category.objects.filter(sub_categories__name=item)

        #     current_url = resolve(self.request.path_info).url_name
        #
        #     if current_url == 'product_category_list_parent':
        #         context['category_list'] = Category.objects.filter(parent__isnull=True)
        #     elif current_url == 'product_category_list_child':
        #         context['category_list'] = Category.objects.filter(parent_id=self.kwargs.get('pk'))
        print('self.kwargs:\n', self.kwargs)
        return context


class CategoryAddView(CreateView):
    model = Category
    form_class = CategoryForm
    # success_url = reverse_lazy('category:list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    # success_url = reverse_lazy('category:list')


class SubCategoryListView(ListView):
    model = SubCategory

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     current_url = resolve(self.request.path_info).url_name
    #
    #     if current_url == 'product_category_list_parent':
    #         context['category_list'] = Category.objects.filter(parent__isnull=True)
    #     elif current_url == 'product_category_list_child':
    #         context['category_list'] = Category.objects.filter(parent_id=self.kwargs.get('pk'))
    #
    #     return context


class SubCategoryAddView(CreateView):
    model = SubCategory


class SubCategoryUpdateView(UpdateView):
    model = SubCategory
