from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from unit.forms import UnitForm, CaseForm
from unit.models import Unit, Case


class UnitListView(ListView):
    model = Unit


class UnitAddView(CreateView):
    model = Unit
    form_class = UnitForm
    success_url = reverse_lazy('unit:list')


class UnitUpdateView(UpdateView):
    model = Unit
    form_class = UnitForm
    success_url = reverse_lazy('unit:list')


class CaseListView(ListView):
    model = Case


class CaseAddView(CreateView):
    model = Case
    form_class = CaseForm
    success_url = reverse_lazy('unit:case_list')


class CaseUpdateView(UpdateView):
    model = Case
    form_class = CaseForm
    success_url = reverse_lazy('unit:case_list')
