from django.db import models
from django.utils.translation import ugettext as _


class Unit(models.Model):
    """
    Единицы измерения
    """
    short_name = models.CharField(max_length=30, verbose_name=_('Краткое название'))
    long_name = models.CharField(max_length=20, verbose_name=_('Полное название'))

    class Meta:
        verbose_name = _('Единица измерения')
        verbose_name_plural = _('Единицы измерения')

    def __str__(self):
        return self.short_name


class Manufacturer(models.Model):
    """
    Произвадители
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))
    address = models.CharField(max_length=300, verbose_name=_('Адрес'), blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True, verbose_name=_('Описание'))
    website = models.URLField(blank=True, null=True, verbose_name=_('URL'))

    class Meta:
        verbose_name = _('Произвадитель')
        verbose_name_plural = _('Произвадители')

    def __str__(self):
        return self.title


class Agriculture(models.Model):
    """
    Что выращиваем? Агрокультура - кукуруза, буряк, пшеница
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))
    photo = models.ImageField(upload_to='reference_books', blank=True, null=True)
    desc = models.TextField(blank=True, null=True, verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Агрокультура')
        verbose_name_plural = _('Агрокультуры')

    def __str__(self):
        return self.title


class Seed(models.Model):
    """
    Семена
    """
    agriculture = models.ForeignKey(Agriculture, on_delete=models.CASCADE, verbose_name=_('Агрокультура'))
    title = models.CharField(max_length=250, verbose_name=_('Название'))
    desc = models.TextField(blank=True, null=True, verbose_name=_('Описание'))
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name=_('Произвадитель'))
    seeding_rate = models.DecimalField(verbose_name=_('Норма высева'), decimal_places=3, max_digits=15)
    seeding_rate_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Семена')
        verbose_name_plural = _('Семена')

    def __str__(self):
        return self.title
