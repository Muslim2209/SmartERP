from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from customer.models import Customer
from erp_user.decorators import allowed_users
from order.models import Order
from tools.config import CONSTANTS


@login_required(login_url='erp_user:login')
@allowed_users(allowed_roles=['admin'])
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    orders_count = orders.count()
    customers_count = customers.count()
    new_orders = orders.filter(status=CONSTANTS.ORDER.STATUS.NEW).count()
    in_progress = orders.filter(status=CONSTANTS.ORDER.STATUS.IN_PROGRESS).count()
    context = {
        'orders': orders,
        'customers': customers,
        'orders_count': orders_count,
        'customers_count': customers_count,
        'new_orders': new_orders,
        'in_progress': in_progress,
    }
    return render(request, 'dashboard/dashboard.html', context)
