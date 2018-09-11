import decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    View,
)
from reference_books.models import (
    Field,
    Agriculture,
    Seed,
    WorkType,
    ProcessCycle,
    WorkAndTechnique,
    FuelCoast,
)


class AddPlanView(LoginRequiredMixin, View):
    login_url = reverse_lazy('user:login')

    def get(self, request):
        params = self.request.GET
        action = params.get('action', False)

        try:
            return getattr(self, '_' + action)(params)
        except:
            agricultures = Agriculture.objects.prefetch_related('work_type').all()
            context = {
                'fields': Field.objects.values('id', 'title').all(),
                'agricultures': agricultures,
            }
            return render(request, 'planning/add-plan.html', context)

    def _get_field_data(self, params):
        field = Field.objects.get(id=params.get('field_id'))
        field_data = {
            'square': field.square,
            'rent_cost': field.rent_cost,
        }
        return JsonResponse({
            'status': True,
            'field_data': field_data,
        })

    def _get_seeds(self, params):
        seeds = [
            {
                'id': i['id'],
                'title': i['title']
            } for i in Seed.objects.values('id', 'title').filter(agriculture_id=params.get('agriculture_id'))
        ]

        return JsonResponse({
            'status': True,
            'seeds': seeds,
        })

    def _get_work_units(self, params):
        units = [{
            'id': i.id,
            'title': i.short_name,
        } for i in WorkType.objects.get(id=params.get('work_id')).units.all()]

        technique = [{
            'id': i.id,
            'farming_techniques': i.farming_techniques.title,
            'fuel_price': FuelCoast.objects.filter(fuel=i.fuel).first().price,
            'data_attr': [
                {'name': 'fuel-price', 'value': FuelCoast.objects.filter(fuel=i.fuel).first().price},
            ]
        } for i in WorkAndTechnique.objects.filter(work_type_id=params.get('work_id'))]

        return JsonResponse({
            'status': True,
            'units': units,
            'technique': technique,
        })

    def _add_plan_item(self, params):
        current_work_id = params.get('current_work_id')
        context = {
            'works': WorkType.objects.all(),
            'process_cycles': ProcessCycle.objects.values('id', 'title').all(),
            'field_square': decimal.Decimal(params.get('field_square'))
        }
        if current_work_id:
            context['current_work_id'] = int(current_work_id)

        return render(self.request, 'planning/partials/_add-plan-table-row.html', context)

    def _get_data_by_work_and_technique(self, params):
        work_and_technique = WorkAndTechnique.objects.get(id=params.get('work_and_technique_id'))

        return JsonResponse({
            'status': True,
            'composition_driver': work_and_technique.composition_driver,
            'composition_others': work_and_technique.composition_others,
            'output_rate': work_and_technique.output_rate,
            'coast_for_output_rate_driver': work_and_technique.coast_for_output_rate_driver,
            'coast_for_output_rate_others': work_and_technique.coast_for_output_rate_others,
            'coefficient_for_quality_driver': work_and_technique.coefficient_for_quality_driver,
            'coefficient_for_quality_others': work_and_technique.coefficient_for_quality_others,
            'fuel_rate': work_and_technique.fuel_rate,
            'period_start': work_and_technique.period_start,
            'period_end': work_and_technique.period_end,
        })
