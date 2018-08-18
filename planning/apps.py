from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PlanningConfig(AppConfig):
    name = 'planning'
    verbose_name = _('Планирование')
