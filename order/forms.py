from django import forms

from order.models import Order, OrderItem


class OrderForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(queryset=OrderItem.objects.all())

    class Meta:
        model = Order
        fields = ['user', 'customer', 'products', 'status', 'deliver_date', 'note']
