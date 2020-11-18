from django import forms

from customer.models import Customer, CustomerGroup


class CustomerGroupForm(forms.ModelForm):
    class Meta:
        model = CustomerGroup
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
