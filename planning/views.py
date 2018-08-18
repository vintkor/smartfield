from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    FormView,
    View,
)
from .models import (
    Plan,
    PlanItem,
)
from reference_books.models import (
    Field,
    Agriculture,
    Seed,
    WorkType,
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

        if params.get('action') == 'get_seeds' and params.get('agriculture_id'):
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

        if params.get('action') == 'add_plan_item':
            context = {
                'works': WorkType.objects.all()
            }
            return render(request, 'planning/partials/_add-plan-table-row.html', context)

        return HttpResponseBadRequest()
