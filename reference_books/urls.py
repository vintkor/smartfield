from django.urls import path
from .views import (
    DeleteAnyRowView,

    CurrencyListView,
    UnitListView,
    ManufacturerListView,
    AgricultureListView,
    SeedListView,
    FieldListView,
    FieldsCreateFormView,
    FuelListView,
    WorkTypeListView,
    FarmingTechniquesListView,
    MachineryListView,
    WorkAndTechniqueListView,
    FertilizerListView,
    ProtectionListView,
    AdditionalExpenditureListView,
    FarmingTechniquesTypeListView,
    MachineryTypeListView,

    ProcessCycleListView,
    ProcessCycleCreateFormView,
)

app_name = 'reference_books'
urlpatterns = [
    path('delete-any-row/<str:model_name>/<int:model_pk>/', DeleteAnyRowView.as_view(), name='delete-any-row'),

    path('currency/', CurrencyListView.as_view(), name='currency'),
    path('unit/', UnitListView.as_view(), name='unit'),
    path('manufacturer/', ManufacturerListView.as_view(), name='manufacturer'),
    path('agriculture/', AgricultureListView.as_view(), name='agriculture'),
    path('seed/', SeedListView.as_view(), name='seed'),

    path('field/', FieldListView.as_view(), name='field'),
    path('field/add/', FieldsCreateFormView.as_view(), name='add-field'),

    path('fuel/', FuelListView.as_view(), name='fuel'),
    path('work-type/', WorkTypeListView.as_view(), name='work-type'),
    path('farming-techniques/', FarmingTechniquesListView.as_view(), name='farming-techniques'),
    path('machinery/', MachineryListView.as_view(), name='machinery'),
    path('work-and-technique/', WorkAndTechniqueListView.as_view(), name='work-and-technique'),
    path('fertilizer/', FertilizerListView.as_view(), name='fertilizer'),
    path('protection/', ProtectionListView.as_view(), name='protection'),
    path('additional-expenditure/', AdditionalExpenditureListView.as_view(), name='additional-expenditure'),
    path('farming-techniques-type/', FarmingTechniquesTypeListView.as_view(), name='farming-techniques-type'),
    path('machinery-type/', MachineryTypeListView.as_view(), name='machinery-type'),

    path('process-cycle/', ProcessCycleListView.as_view(), name='process-cycle'),
    path('process-cycle/add/', ProcessCycleCreateFormView.as_view(), name='process-cycle-add'),
]
