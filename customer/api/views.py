from django.shortcuts import render

from customer.models import Customer
from order.filters import OrderFilter


def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'customer/customer_list.html', context)


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
