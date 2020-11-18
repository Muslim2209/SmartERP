from django import forms

from product.models import Product, ProductGroup, ProductSubGroup


class ProductGroupForm(forms.ModelForm):
    class Meta:
        model = ProductGroup
        fields = '__all__'


class ProductSubGroupForm(forms.ModelForm):
    class Meta:
        model = ProductSubGroup
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
