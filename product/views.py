from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from product.forms import ProductAddForm
from product.models import Product


def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product/products.html', context)


def product_add(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('product:list'))

    else:
        form = ProductAddForm()

    return render(request, 'product/product_add.html', {'form': form})
