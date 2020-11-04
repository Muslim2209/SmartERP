from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from customer.models import Customer
from erp_user.decorators import unauthenticated_user, allowed_users
from erp_user.forms import CreateUserForm, CustomerForm
from tools.config import CONSTANTS


@allowed_users(allowed_roles=['customer'])
def user_page(request):
    orders = request.user.orders.all()
    orders_count = orders.count()
    new_orders = orders.filter(status=CONSTANTS.ORDER.STATUS.NEW).count()
    in_progress = orders.filter(status=CONSTANTS.ORDER.STATUS.IN_PROGRESS).count()

    context = {
        'orders': orders,
        'orders_count': orders_count,
        'new_orders': new_orders,
        'in_progress': in_progress,
    }
    return render(request, 'user/user.html', context)


@login_required(login_url='erp_user:login')
@allowed_users(allowed_roles=['customer'])
def account_settings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'user/account_settings.html', context)


@unauthenticated_user
def register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group, _ = Group.objects.get_or_create(name='customer')
            user.groups.add(group)
            Customer.objects.create(user=user)
            messages.success(request, 'Account was created for ' + username)
            return redirect('erp_user:login')
    context = {'form': form}
    return render(request, 'user/register.html', context)


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')
        else:
            messages.info(request, 'Username or password is incorrect.')
    context = {}
    return render(request, 'user/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('erp_user:login')
