from django.template import Library, loader, Context
from django.template import RequestContext

from menus.models import *

register = Library()

@register.simple_tag(takes_context=True)
def menu_position(context, position, template='menus/menu_list.html', *args, **kwargs):
    try:
        menu = Menu.objects.prefetch_related('items').get(
            enabled=True,
            position=position
        )
    except (Menu.DoesNotExist, Menu.MultipleObjectsReturned):
        return ''
    else:
        t = loader.get_template(template)

        try:
            links = Link.objects.all()
            active_link = None
            for link in links:
                if link.get_url() == context['request'].path:
                    active_link = link
                    # TODO be more defensive.
                    break

            if active_link is not None:

                context['active_menu_item'] = MenuItem.objects.get(
                    link=active_link)

                if context['active_menu_item']:

                    if context['active_menu_item'].parent:
                        parent = context['active_menu_item'].parent
                    else:
                        parent = context['active_menu_item']

                    context['active_menu_item_children'] = MenuItem.objects.filter(
                        parent=parent)

        except MenuItem.DoesNotExist:
            pass

        context['menu'] = menu

        return t.render(context)
