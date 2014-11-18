import random
import string
import factory

from models import Link, Menu, MenuItem


class LinkFactory(factory.Factory):
    class Meta:
        model = Link

    title = factory.Sequence(lambda n: 'Link%d' % n)
    url = factory.Sequence(lambda n: 'Url%d' % n)


class MenuFactory(factory.Factory):
    class Meta:
        model = Menu

    title = factory.Sequence(lambda n: 'Menu%d' % n)
    enabled = random.random < 0.3


class MenuItemFactory(factory.Factory):
    class Meta:
        model = MenuItem

    menu = factory.SubFactory(MenuFactory)
    link = factory.SubFactory(LinkFactory)
    order = 0
    is_featured = random.random < 0.3
    parent = None
