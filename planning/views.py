from django.shortcuts import render
from django.views.generic import (
    FormView,
    View,
)
from .models import (
    Plan,
    PlanItem,
)


class AddPlanView(View):

    def get(self, request):
        context = {}
        return render(request, 'planning/add-plan.html', context)
