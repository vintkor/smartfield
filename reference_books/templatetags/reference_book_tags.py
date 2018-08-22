from django import template


register = template.Library()


@register.inclusion_tag('reference_books/partials/_buttons.html')
def insert_action_buttons(model_name, instance):
    return {
        'model_name': model_name,
        'instance': instance,
    }
