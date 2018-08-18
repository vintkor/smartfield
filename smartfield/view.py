from django.shortcuts import render
from django.views import View
from company.models import Company


class DashboardView(View):

    def get(self, request):
        context = {
            'company': Company.objects.first()
        }
        return render(request, 'cabinet/index.html', context)
