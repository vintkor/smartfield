from django.db import models
from django.utils.translation import ugettext as _


class Company(models.Model):
    """
    Компания
    """
    short_name = models.CharField(verbose_name=_('Краткое название'), max_length=100)
    full_name = models.CharField(verbose_name=_('Полное название'), max_length=100)

    class Meta:
        verbose_name = _('Компания')

    def __str__(self):
        return self.short_name
