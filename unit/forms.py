from django import forms

from unit.models import Unit, Case


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
