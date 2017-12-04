# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('userproperty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalproperty',
            name='name',
            field=models.SlugField(max_length=64, verbose_name='name', unique=True),
        ),
        migrations.AlterField(
            model_name='userproperty',
            name='name',
            field=models.SlugField(max_length=64, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='userproperty',
            name='user',
            field=models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL, related_name='user_properties'),
        ),
    ]
