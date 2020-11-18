from django import forms

from price.models import Price, Currency


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = '__all__'


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'
