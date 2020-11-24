from django import forms
from django.forms import formset_factory

from warehouse.models import *


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'


# StockFormSet = formset_factory(StockForm)


class ProductTransactionForm(forms.ModelForm):
    class Meta:
        model = ProductTransaction
        fields = '__all__'


class TransactionItemForm(forms.ModelForm):
    class Meta:
        model = TransactionItem
        fields = '__all__'


ProductTransactionFormset = forms.inlineformset_factory(ProductTransaction, TransactionItem,
                                                        fields=['product', 'price', 'quantity'],
                                                        form=TransactionItemForm,
                                                        extra=1)

# class WarehouseBalanceForm(forms.ModelForm):
#     class Meta:
#         model = Balance
#         fields = '__all__'
