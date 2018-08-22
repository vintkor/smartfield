from django.http import JsonResponse
from django.views import View
from .models import (
    Currency,
    Unit,
    Manufacturer,
    Agriculture,
    Seed,
    Field,
    Fuel,
    WorkType,
    FarmingTechniques,
    Machinery,
    WorkAndTechnique,
    Fertilizer,
    Protection,
    AdditionalExpenditure,
    FarmingTechniquesType,
    MachineryType,
    ProcessCycle,
)
from django.views.generic import (
    ListView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import FieldsCreateForm
from django.utils.translation import ugettext as _
from .forms import (
    ProcessCycleCreateForm,
)
from django.apps import apps


class DeleteAnyRowView(LoginRequiredMixin, View):
    """
    Удаление любой записи в моделях справочников по параметрам
    """
    login_url = reverse_lazy('user:login')

    def post(self, request, model_name, model_pk):
        model = apps.get_model(app_label='reference_books', model_name=model_name)
        try:
            model_item = model.objects.get(pk=model_pk)
        except model.DoesNotExist:
            return JsonResponse({
                'status': False,
            })

        model_item.delete()
        return JsonResponse({
            'status': True,
        })


class CurrencyListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/currencies-list-view.html'
    context_object_name = 'currencies'
    model = Currency


class UnitListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/units-list-view.html'
    context_object_name = 'units'
    model = Unit


class ManufacturerListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/manufacturers-list-view.html'
    context_object_name = 'manufacturers'
    model = Manufacturer


class AgricultureListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/agriculturies-list-view.html'
    context_object_name = 'agriculturies'
    model = Agriculture


class SeedListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/seeds-list-view.html'
    context_object_name = 'seeds'
    model = Seed


class FieldListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/fields-list-view.html'
    context_object_name = 'fields'
    model = Field


class FieldsCreateFormView(CreateView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/fields-add-form-view.html'
    form_class = FieldsCreateForm


class FuelListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/fuels-list-view.html'
    context_object_name = 'fuels'
    model = Fuel


class WorkTypeListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/work_types-list-view.html'
    context_object_name = 'work_types'
    model = WorkType


class FarmingTechniquesListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/farming_techniques-list-view.html'
    context_object_name = 'farming_techniques'
    model = FarmingTechniques


class MachineryListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/machineries-list-view.html'
    context_object_name = 'machineries'
    model = Machinery


class WorkAndTechniqueListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/work_and_technique-list-view.html'
    context_object_name = 'work_and_technique'
    model = WorkAndTechnique


class FertilizerListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/fertilizers-list-view.html'
    context_object_name = 'fertilizers'
    model = Fertilizer


class ProtectionListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/protections-list-view.html'
    context_object_name = 'protections'
    model = Protection


class AdditionalExpenditureListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/additional_expenditure-list-view.html'
    context_object_name = 'additional_expenditure'
    model = AdditionalExpenditure


class FarmingTechniquesTypeListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/farming_techniques_types-list-view.html'
    context_object_name = 'farming_techniques_types'
    model = FarmingTechniquesType


class MachineryTypeListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/machinery_types-list-view.html'
    context_object_name = 'machinery_types'
    model = MachineryType


class ProcessCycleListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'reference_books/process_cycles-list-view.html'
    context_object_name = 'process_cycles'
    model = ProcessCycle

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['actions'] = [
            {
                'title': _('Добавить цикл'),
                'url': reverse_lazy('reference_books:process-cycle-add'),
                'icon_class': 'la la-plus',
            }
        ]
        return context


class ProcessCycleCreateFormView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('user:login')
    form_class = ProcessCycleCreateForm
    template_name = 'reference_books/process_cycles-create-view.html'
    success_url = reverse_lazy('reference_books:process-cycle')
