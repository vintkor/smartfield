import decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseBadRequest
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
)


class AddPlanView(LoginRequiredMixin, View):
    login_url = reverse_lazy('user:login')

    def get(self, request):
        print('-'*80)
        params = self.request.GET
        print(params)

        if not params:
            context = {
                'fields': Field.objects.values('id', 'title').all(),
                'agricultures': Agriculture.objects.values('id', 'title').all(),
            }
            return render(request, 'planning/add-plan.html', context)

        action = params.get('action')

        if action == 'get_field_data' and params.get('field_id'):
            field = Field.objects.get(id=params.get('field_id'))
            field_data = {
                'square': field.square,
                'rent_cost': field.rent_cost,
            }
            return JsonResponse({
                'status': True,
                'field_data': field_data,
            })

        if action == 'get_seeds' and params.get('agriculture_id'):
            seeds = [
                {
                    'id': i['id'],
                    'title': i['title'],
                } for i in Seed.objects.values('id', 'title').filter(agriculture_id=params.get('agriculture_id'))
            ]

            return JsonResponse({
                'status': True,
                'seeds': seeds,
            })

        if action == 'get_work_units' and params.get('work_id'):
            units = [{
                'id': i.id,
                'title': i.short_name,
            } for i in WorkType.objects.get(id=params.get('work_id')).units.all()]

            technique = [{
                'id': i.id,
                'farming_techniques': i.farming_techniques.title,
            } for i in WorkAndTechnique.objects.filter(work_type_id=params.get('work_id'))]

            return JsonResponse({
                'status': True,
                'units': units,
                'technique': technique,
            })

        if action == 'add_plan_item' and params.get('field_square'):
            context = {
                'works': WorkType.objects.all(),
                'process_cycles': ProcessCycle.objects.values('id', 'title').all(),
                'field_square': decimal.Decimal(params.get('field_square')),
            }
            return render(request, 'planning/partials/_add-plan-table-row.html', context)

        if action == 'get_data_by_work_and_technique' and params.get('work_and_technique_id'):
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
            })

        return HttpResponseBadRequest()
