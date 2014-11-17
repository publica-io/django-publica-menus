from django import template
from menus.models import Menu

register = template.Library()

@register.inclusion_tag('menus/menu_list.html', takes_context=True)
def menu(context, slug, *args, **kwargs):
    request = context['view'].request

    try:
        query = Menu.objects.get(
            enabled=True,
            slug=slug
            )
    except Menu.DoesNotExist, Menu.MultipleObjectsReturned:
        query = None

    context["menu"] = query

    return context
