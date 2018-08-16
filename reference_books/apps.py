from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ReferenceBooksConfig(AppConfig):
    name = 'reference_books'
    verbose_name = _('Справочники')
