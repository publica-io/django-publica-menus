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
    except Menu.DoesNotExist, Menu.MultipleObjectsReturned:
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


@register.simple_tag(takes_context=True)
def get_active_parent_or_child(context, template='menus/menu_parent_child.html', parent=True):
    """
        The code would do the following:
        given the url get active link, if it is parent link then return all parents
        if child then return parent with all its children

        Takes input if all parent links are wanted all or all children links are wanted
    """


    # import ipdb; ipdb.set_trace()


    current_url = context['request'].path
    active_child_url = None
    active_parent_url = None
    menu = context['menu']

    try:
        menu_item = MenuItem.objects.get(
            link__url=current_url,
        )

    except MenuItem.DoesNotExist:
        # This means that there is no link or is linke to a menu but is requesting a menu
        # menu_item = MenuItem.objects.get(link__url='/')
        # pass
        menu_item = None

    except MenuItem.MultipleObjectsReturned:
        #..TODO.. A better way to handle this case.
        menu_item = MenuItem.objects.filter(link__url=current_url).first()
    

    # If the link is child
    if menu_item and menu_item.parent is not None:
        active_child_url = menu_item.link.get_url()
        active_parent_url = menu_item.parent.link.get_url()
        menu_item = menu_item.parent.children.all()
    else:
        active_parent_url = menu_item.link.get_url()
        menu_item = menu_item.children.all()


    t = loader.get_template(template)

    context.update({
        'parent': parent,
        'menu_item': menu_item,
        'active_child_url': active_child_url,
        'active_parent_url': active_parent_url,

        })
    
    return t.render(context)
