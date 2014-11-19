from django.template import Library, loader, Context
from django.template import RequestContext

from menus.models import Menu, MenuItem

register = Library()

@register.simple_tag(takes_context=True)
def menu(context, slug, template='menus/menu_list.html', *args, **kwargs):
    try:
        menu = Menu.objects.prefetch_related('items').get(
            enabled=True,
            slug=slug
        )
    except Menu.DoesNotExist, Menu.MultipleObjectsReturned:
        menu = None

    t = loader.get_template(template)
    return t.render(Context({
        'menu': menu,
        'request': context['request']
    }))


@register.simple_tag(takes_context=True)
<<<<<<< HEAD
def get_active_parent_or_child(context, template, parent=True):
    """
        The code would do the following:
        given the url get active link, if it is parent link then return all parents
        if child then return parent with all its children

        Takes input if all parent links are wanted all or all children links are wanted
=======
def get_active_parent_or_child(context, template):
    """
        The code would do the following:
        given the url get active link, if parent just return children
        if child then return parent with all its children
>>>>>>> d17d3b9ab0de1d33e12ed2387c7a9bc874e64d82
    """

    current_url = context['request'].path
    active_child_url = None
<<<<<<< HEAD
    active_parent_url = None
    menu = ''

=======
>>>>>>> d17d3b9ab0de1d33e12ed2387c7a9bc874e64d82
    try:
        menu_item = MenuItem.objects.get(
            link__url=current_url,
        )

    except MenuItem.DoesNotExist, MenuItem.MultipleObjectsReturned:
        menu_item = None
<<<<<<< HEAD
    # Well get the menu either way
    try:
        menu = Menu.objects.prefetch_related('items').get(
            enabled=True,
            slug=menu_item.menu.slug
        )
    except Menu.DoesNotExist, Menu.MultipleObjectsReturned:
        menu = None
=======
>>>>>>> d17d3b9ab0de1d33e12ed2387c7a9bc874e64d82

    # If the link is child
    if menu_item and menu_item.parent is not None:
        active_child_url = menu_item.link.get_url()
<<<<<<< HEAD
        active_parent_url = menu_item.parent.link.get_url()
        menu_item = menu_item.parent.children.all()
    else:
        active_parent_url = menu_item.link.get_url()
        menu_item = menu_item.children.all()


=======
        menu_item = menu_item.parent.children.all()
    else:
        menu = Menu.objects.prefetch_related('items').get(
            enabled=True,
            slug=slug
        )
        except Menu.DoesNotExist, Menu.MultipleObjectsReturned:
            menu = None
        

    
    
>>>>>>> d17d3b9ab0de1d33e12ed2387c7a9bc874e64d82
    t = loader.get_template(template)
    return t.render(Context({
        'menu': menu,
        'menu_item': menu_item,
        'active_child_url': active_child_url,
<<<<<<< HEAD
        'active_parent_url': active_parent_url,
        'request': context['request'],
        'parent': parent
    }))
=======
        'request': context['request']
    }))

>>>>>>> d17d3b9ab0de1d33e12ed2387c7a9bc874e64d82
