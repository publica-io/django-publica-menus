# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import images.mixins
import entropy.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('url', models.CharField(help_text=b'Optionally, override and link to an arbitrary URL', max_length=1024, blank=True)),
                ('title', models.CharField(max_length=255)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'verbose_name': 'Link URL',
                'verbose_name_plural': "Link URLs (Re-useable for Menu's)",
            },
            bases=(models.Model, images.mixins.ImageMixin),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('short_title', models.CharField(max_length=255, blank=True)),
                ('slug', models.SlugField(max_length=255)),
                ('enabled', models.BooleanField(default=False, db_index=True)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': "Menu's (with Link URLs)",
            },
            bases=(entropy.mixins.BaseSlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('link', models.ForeignKey(related_name='links', to='menus.Link')),
                ('menu', models.ForeignKey(related_name='items', to='menus.Menu')),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='menus.MenuItem', null=True)),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Menu Item with Link URL',
                'verbose_name_plural': 'Menu Items that use Link URLs',
            },
            bases=(models.Model,),
        ),
    ]
