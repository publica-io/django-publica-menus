from django import template
from menus.models import Menu

register = template.Library()

@register.inclusion_tag('menus/menu_list.html')
def menu(slug, *args, **kwargs):
    try:
        menu = Menu.objects.get(
            enabled=True,
            slug=slug
        )
    except Menu.DoesNotExist, Menu.MultipleObjectsReturned:
        menu = None

    return menu
