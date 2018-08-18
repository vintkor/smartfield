from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from reference_books.models import (
    Field,
    Agriculture,
    Seed,
    WorkType,
)
from django.utils.translation import ugettext as _
from django.core import serializers


class DemoView(View):

    def get(self, request):
        params = self.request.GET
        print('-'*80)
        print(params)

        # Если нет параметров - отдаём HTML
        if not params:
            return render(request, 'demo.html')

        if params.get('action') == 'initialData':
            data = dict()
            data['fields'] = serializers.serialize('json', Field.objects.all())
            data['agriculture'] = serializers.serialize('json', Agriculture.objects.all())
            data['works'] = serializers.serialize('json', WorkType.objects.all())

            return JsonResponse(data)

        # Получение доступных семян
        if params.get('action') == 'getSeeds':
            agriculture_id = params.get('agricultureID')[0]

            return JsonResponse({
                'status': True,
                'seeds': [{
                    'id': seed.id,
                    'title': seed.title,
                    'seeding_rate': seed.seeding_rate,
                    'seeding_rate_unit': str(seed.seeding_rate_unit),
                } for seed in Seed.objects.filter(agriculture_id=agriculture_id)]
            })

        return JsonResponse({
            'status': False,
            'message': _('Не верный формат запроса')
        })
