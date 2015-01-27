# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField(unique=True, max_length=64, verbose_name=b'tag')),
                ('value', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Global Property',
                'verbose_name_plural': 'Global Properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField(max_length=64, verbose_name=b'tag')),
                ('value', models.CharField(max_length=256)),
                ('user', models.ForeignKey(related_name='userprop', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Property',
                'verbose_name_plural': 'User Properties',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='userproperty',
            unique_together=set([('user', 'name')]),
        ),
    ]
