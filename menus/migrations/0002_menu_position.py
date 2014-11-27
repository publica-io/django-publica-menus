# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='position',
            field=models.CharField(default='main-menu', max_length=50, choices=[(b'main-menu', b'Main Menu'), (b'footer-left-menu', b'Footer Menu'), (b'footer-social-menu', b'Footer Left - Social Icons'), (b'footer-right-menu', b'Footer Right (Logos)')]),
            preserve_default=False,
        ),
    ]
