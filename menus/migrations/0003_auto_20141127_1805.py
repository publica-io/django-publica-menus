# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def fix_menus(apps, schema_editor):
    Menu = apps.get_model('menus', 'Menu')

    new_vals = {
        'home-menu': 'main-menu',
        'home-menu-1': 'main-menu',
        'home-footer-social': 'footer-social-menu',
        'home-footer-links': 'footer-left-menu',
        'home-footer-logos': 'footer-right-menu'
    }
    for menu in Menu.objects.all():
        try:
            menu.position = new_vals[menu.slug]
        except:
            print 'No new value for {}'.format(menu.slug)


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_menu_position'),
    ]

    operations = [
        migrations.RunPython(fix_menus),
    ]
