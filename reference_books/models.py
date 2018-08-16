from django.utils.translation import ugettext as _
from django.contrib.gis.db import models


class Unit(models.Model):
    """
    Единицы измерения
    """
    short_name = models.CharField(max_length=30, verbose_name=_('Краткое название'))
    long_name = models.CharField(max_length=20, verbose_name=_('Полное название'))

    class Meta:
        verbose_name = _('Единица измерения')
        verbose_name_plural = _('Единицы измерения')
        ordering = ('long_name',)

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
    seeding_rate_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name=_('Ед. измерения'))

    class Meta:
        verbose_name = _('Семена')
        verbose_name_plural = _('Семена')

    def __str__(self):
        return self.title


class Field(models.Model):
    """
    Карта полей
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))
    desc = models.TextField(blank=True, null=True, verbose_name=_('Описание'))
    polygon = models.PolygonField(verbose_name=_('Полигон поля'), geography=True)
    square = models.DecimalField(verbose_name=_('Площадь'), blank=True, null=True, decimal_places=6, max_digits=30)
    square_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name=_('Ед. измерения'), blank=True, null=True)
    rent_cost = models.DecimalField(verbose_name=_('Стоимость аренды'), blank=True, null=True, decimal_places=3, max_digits=10)

    class Meta:
        verbose_name = _('Поле')
        verbose_name_plural = _('Поля')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.square is None:
            self.square = self.polygon.transform(3587, clone=True).area / 10000
        return super(Field, self).save(*args, **kwargs)


class Fuel(models.Model):
    """
    Топливо
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))

    class Meta:
        verbose_name = _('Топливо')
        verbose_name_plural = _('Топливо')
        ordering = ('title',)

    def __str__(self):
        return self.title


class WorkType(models.Model):
    """
    Вид работ
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))
    desc = models.TextField(blank=True, null=True, verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Вид работ')
        verbose_name_plural = _('Виды работ')
        ordering = ('title',)

    def __str__(self):
        return self.title


class FarmingTechniques(models.Model):
    """
    Самоходная техника
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))
    photo = models.ImageField(upload_to='reference_books', blank=True, null=True)
    desc = models.TextField(blank=True, null=True, verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Самоходная техника')
        verbose_name_plural = _('Самоходная техника')
        ordering = ('title',)

    def __str__(self):
        return self.title


class Machinery(models.Model):
    """
    Прицепные аггрегаты
    """
    farming_techniques = models.ForeignKey(FarmingTechniques, on_delete=models.CASCADE, verbose_name=_('Самоходная техника'))
    title = models.CharField(max_length=250, verbose_name=_('Название'))
    photo = models.ImageField(upload_to='reference_books', blank=True, null=True)
    desc = models.TextField(blank=True, null=True, verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Прицепной аггрегат')
        verbose_name_plural = _('Прицепные аггрегаты')
        ordering = ('title',)

    def __str__(self):
        return self.title


class WorkAndTechnique(models.Model):
    """
    Работа и техника
    """
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE, verbose_name=_('Вид работ'))
    farming_techniques = models.ForeignKey(FarmingTechniques, on_delete=models.CASCADE, verbose_name=_('Самоходная техника'))
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE, verbose_name=_('Прицепной аггрегат'), blank=True, null=True)
    fuel_rate = models.DecimalField(verbose_name=_('Расход топлива'), decimal_places=4, max_digits=10)
    fuel_rate_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name=_('Ед. измерения расхода топлива'))

    class Meta:
        verbose_name = _('Работа и техника')
        verbose_name_plural = _('Работа и техника')

    def __str__(self):
        return '{} {}'.format(self.work_type, self.farming_techniques)
