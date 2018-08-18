from django.contrib.auth.mixins import LoginRequiredMixin
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
)


class AddPlanView(LoginRequiredMixin, View):
    login_url = reverse_lazy('user:login')

    def get(self, request):
        context = {
            'fields': Field.objects.values('id', 'title').all(),
            'agricultures': Agriculture.objects.values('id', 'title').all(),
        }
        return render(request, 'planning/add-plan.html', context)
