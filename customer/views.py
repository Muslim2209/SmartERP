from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from customer.forms import CustomerAddForm
from customer.models import Customer
from order.filters import OrderFilter


def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'customer/customers.html', context)


def customer_detail(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.orders.all()
    total_orders = orders.count()
    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs
    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders,
        'my_filter': my_filter,
    }
    return render(request, 'customer/customer_detail.html', context)


def customer_add(request):
    if request.method == 'POST':
        form = CustomerAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('customer:list'))

    else:
        form = CustomerAddForm()

    return render(request, 'customer/customer_add.html', {'form': form})
