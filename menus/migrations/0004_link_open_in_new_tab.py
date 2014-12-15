# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_auto_20141127_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='open_in_new_tab',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
