from django.db import models
from django.utils.translation import ugettext as _
from reference_books.models import (
    WorkType,
    Unit,
    ProcessCycle,
    WorkAndTechnique,
    Field,
    Agriculture,
    Seed,
)


class Plan(models.Model):
    """
    План
    """
    title = models.CharField(max_length=250, verbose_name=_('Заголовок'))
    field = models.ForeignKey(Field, on_delete=models.CASCADE, verbose_name=_('Поле'))
    agriculture = models.ForeignKey(Agriculture, on_delete=models.CASCADE, verbose_name=_('Агрокультура'))
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE, verbose_name=_('Семена'))
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_('Дата создания'))
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name=_('Дата обновления'))

    class Meta:
        verbose_name = _('План')
        verbose_name_plural = _('Планы')

    def __str__(self):
        return self.title


class PlanItem(models.Model):
    """
    Строка плана
    """
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name=_('План'))
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE, verbose_name=_('Вид работ'))
    work_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name=_('Ед. измерения работы'))
    process_cycle = models.ForeignKey(ProcessCycle, on_delete=models.CASCADE, verbose_name=_('Технологический цикл'))
    period_start = models.DateField(verbose_name=_('Период - с'))
    period_end = models.DateField(verbose_name=_('Период - по'))
    work_and_technique = models.ForeignKey(WorkAndTechnique, on_delete=models.CASCADE, verbose_name=_('Техника'))
    machine_operator = models.PositiveSmallIntegerField(verbose_name=_('Мехинизаторы'))
    other_operator = models.PositiveSmallIntegerField(verbose_name=_('Другие работники'))
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_('Дата создания'))
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name=_('Дата обновления'))

    class Meta:
        verbose_name = _('Строка плана')
        verbose_name_plural = _('Строки плана')

    def __str__(self):
        return '{}, '.format(self.plan.title[:30])
