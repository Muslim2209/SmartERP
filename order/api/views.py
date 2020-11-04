from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from customer.models import Customer
from order.forms import OrderForm
from order.models import Order, OrderItem


@login_required(login_url='erp_user:login')
def order(request):
    return render(request, 'order/status.html')


@login_required(login_url='erp_user:login')
def create_order(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, exclude=['customer'])
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('dashboard:dashboard')
    context = {
        'formset': formset
    }
    return render(request, 'order/order_form.html', context)


@login_required(login_url='erp_user:login')
def update_order(request, pk):
    order_obj = Order.objects.get(id=pk)
    form = OrderForm(instance=order_obj)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order_obj)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard')
    context = {
        'form': form
    }
    return render(request, 'order/order_form.html', context)


@login_required(login_url='erp_user:login')
def delete_order(request, pk):
    item = Order.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard:dashboard')
    context = {
        'item': item,
    }
    return render(request, 'order/delete_confirm.html', context)
