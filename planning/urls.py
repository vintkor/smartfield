from django.urls import path
from .views import (
    AddPlanView,
)


app_name = 'planning'
urlpatterns = [
    path('add-plan/', AddPlanView.as_view(), name='add-plan'),
]
