from django.contrib.gis import forms
from .models import (
    Field,
    ProcessCycle,
)
from django.conf import settings
from django.contrib.gis.forms import widgets
from django.utils.translation import ugettext_lazy as _


# class GoogleWidget(widgets.OSMWidget):
class GoogleWidget(widgets.OpenLayersWidget):
    # template_name = 'gis/openlayers-osm.html'
    default_lon = 3503050
    default_lat = 6278821
    default_zoom = 6
    map_width = 1000
    map_height = 600


class FieldsCreateForm(forms.ModelForm):
    polygon = forms.CharField(widget=GoogleWidget())

    class Meta:
        model = Field
        fields = (
            'title',
            'desc',
            'polygon',
            'square',
            'square_unit',
            'rent_cost',
            'rent_cost_unit',
            'rent_cost_currency',
        )

    class Media:
        js = (
            "https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/OpenLayers.js",
            "https://maps.googleapis.com/maps/api/js?key={0}".format(settings.GOOGLE_MAPS_API_KEY)
        )


class ProcessCycleCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label=_('Название'))
    sort = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label=_('Сортировка'))

    class Meta:
        model = ProcessCycle
        fields = (
            'title',
            'sort',
        )
