from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View


class DashboardView(LoginRequiredMixin, View):
    login_url = reverse_lazy('user:login')

    def get(self, request):
        context = {
            'show_fake_data': True
        }
        return render(request, 'cabinet/index.html', context)
