from django import template
from company.models import Company


register = template.Library()


@register.simple_tag
def get_company():
    return Company.objects.first()
