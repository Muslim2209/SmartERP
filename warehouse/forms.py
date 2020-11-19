from django import forms

from warehouse.models import Warehouse, WarehouseInput, Balance, InputProduct


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'


class WarehouseInputForm(forms.ModelForm):
    class Meta:
        model = WarehouseInput
        fields = '__all__'


class InputProductForm(forms.ModelForm):
    class Meta:
        model = InputProduct
        fields = '__all__'


InputProductFormset = forms.inlineformset_factory(WarehouseInput, InputProduct, form=InputProductForm, extra=1)


class WarehouseBalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = '__all__'
