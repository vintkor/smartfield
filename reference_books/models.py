from django.utils.translation import ugettext as _
from django.contrib.gis.db import models
from django.core.exceptions import ValidationError


def iso_4217_numeric_code_validator(value):
    if not len(str(value)) == 3:
        raise ValidationError(_(
            'Код "{}" дожен быть трёхзначным'.format(value)
        ))


class Currency(models.Model):
    """
    Валюта
    """
    title = models.CharField(max_length=100, verbose_name=_('Название'))
    iso_4217_letter_code = models.CharField(max_length=3, verbose_name=_('ISO 4217 символьный код'))
    iso_4217_numeric_code = models.PositiveSmallIntegerField(verbose_name=_('ISO 4217 цыфровой код'), validators=[iso_4217_numeric_code_validator])
    short_symbol = models.CharField(verbose_name=_('Символ'), max_length=5, blank=True, null=True)
    is_main = models.BooleanField(default=False, verbose_name=_('Является основной'))

    class Meta:
        verbose_name = _('Валюта')
        verbose_name_plural = _('Валюты')

    def __str__(self):
        return self.title


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
    work_type = models.ManyToManyField('reference_books.WorkType')

    class Meta:
        verbose_name = _('Агрокультура')
        verbose_name_plural = _('Агрокультуры')
        ordering = ('id',)

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
    rent_cost_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='rent_cost_unit', verbose_name=_('Ед. измерения стоимости аренды'), blank=True, null=True)
    rent_cost_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name=_('Валюта стоимости аренды'), blank=True, null=True)

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


class FuelCoast(models.Model):
    """
    Стоимость топлива
    """
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, verbose_name=_('Топливо'))
    price = models.DecimalField(max_digits=10, decimal_places=4, verbose_name=_('Цена'))
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_('Дата создания'))

    class Meta:
        verbose_name = _('Стоимость топлива')
        verbose_name_plural = _('Стоимость топлива')

    def __str__(self):
        return str(self.price)


class WorkType(models.Model):
    """
    Вид работ
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))
    desc = models.TextField(blank=True, null=True, verbose_name=_('Описание'))
    sort = models.PositiveSmallIntegerField(default=10, verbose_name=_('Сортировка'))
    units = models.ManyToManyField(Unit, verbose_name=_('Ед. измерения'))

    class Meta:
        verbose_name = _('Вид работ')
        verbose_name_plural = _('Виды работ')
        ordering = ('sort', 'title')

    def __str__(self):
        return self.title


class FarmingTechniquesType(models.Model):
    """
    Тип самоходной техники
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))

    class Meta:
        verbose_name = _('Тип самоходной техники')
        verbose_name_plural = _('Типы самоходной техники')
        ordering = ('title',)

    def __str__(self):
        return self.title


class MachineryType(models.Model):
    """
    Тип прицепных агрещатов
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))

    class Meta:
        verbose_name = _('Тип прицепных агрещатов')
        verbose_name_plural = _('Типы прицепных агрещатов')
        ordering = ('title',)

    def __str__(self):
        return self.title


class FarmingTechniques(models.Model):
    """
    Самоходная техника
    """
    type = models.ForeignKey(FarmingTechniquesType, on_delete=models.CASCADE)
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
    type = models.ForeignKey(MachineryType, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name=_('Название'))
    photo = models.ImageField(upload_to='reference_books', blank=True, null=True)
    desc = models.TextField(blank=True, null=True, verbose_name=_('Описание'))
    farming_techniques = models.ManyToManyField(FarmingTechniques, verbose_name=_('Самоходная техника'))

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
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, verbose_name=_('Топливо'))
    fuel_rate = models.DecimalField(verbose_name=_('Расход топлива'), decimal_places=4, max_digits=10)
    fuel_rate_unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name=_('Ед. измерения расхода топлива'))
    composition_driver = models.PositiveSmallIntegerField(verbose_name=_('Состав аггрегата - механизаторы'), blank=True, null=True)
    composition_others = models.PositiveSmallIntegerField(verbose_name=_('Состав аггрегата - другие'), blank=True, null=True)
    output_rate = models.DecimalField(max_digits=15, decimal_places=4, verbose_name=_('Норма выработки'), blank=True, null=True)
    coast_for_output_rate_driver = models.DecimalField(
        max_digits=15, decimal_places=4, verbose_name=_('Оплата за норму по тарифу - механизаторы'), blank=True, null=True)
    coast_for_output_rate_others = models.DecimalField(
        max_digits=15, decimal_places=4, verbose_name=_('Оплата за норму по тарифу - другие'), blank=True, null=True)
    coefficient_for_quality_driver = models.DecimalField(
        max_digits=5, decimal_places=3, verbose_name=_('Коэфициент за качество - механизаторы'), blank=True, null=True)
    coefficient_for_quality_others = models.DecimalField(
        max_digits=5, decimal_places=3, verbose_name=_('Коэфициент за качество - другие'), blank=True, null=True)

    class Meta:
        verbose_name = _('Работа и техника')
        verbose_name_plural = _('Работа и техника')

    def __str__(self):
        return '{} {}'.format(self.work_type, self.farming_techniques)


class Fertilizer(models.Model):
    """
    Удобрения
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Производитель'))
    desc = models.TextField(blank=True, null=True, verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Удобрение')
        verbose_name_plural = _('Удобрения')
        ordering = ('title',)

    def __str__(self):
        return self.title


class Protection(models.Model):
    """
    Средства защиты растений
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Производитель'))
    desc = models.TextField(blank=True, null=True, verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Средство защиты растений')
        verbose_name_plural = _('Средства защиты растений')
        ordering = ('title',)

    def __str__(self):
        return self.title


class AdditionalExpenditure(models.Model):
    """
    Дополнительные затраты
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))

    class Meta:
        verbose_name = _('Дополнительные затраты')
        verbose_name_plural = _('Дополнительные затраты')
        ordering = ('title',)

    def __str__(self):
        return self.title


class ProcessCycle(models.Model):
    """
    Технологический цикл
    """
    title = models.CharField(max_length=250, verbose_name=_('Название'))
    sort = models.PositiveSmallIntegerField(default=1, verbose_name=_('Сортировка'))

    class Meta:
        verbose_name = _('Технологический цикл')
        verbose_name_plural = _('Технологические циклы')
        ordering = ('sort',)

    def __str__(self):
        return self.title
