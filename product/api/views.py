from django.shortcuts import render

from product.models import Product


def product(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product/products.html', context)
