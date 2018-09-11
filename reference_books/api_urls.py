from django.urls import path
from .api_views import (
    CurrencyListApi,
    UnitListApi,
)


urlpatterns = [
    path('currency', CurrencyListApi.as_view()),
    path('unit', UnitListApi.as_view()),
]
