# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='rate',
            field=models.FloatField(blank=True, verbose_name='Доля ставки', default='1.0'),
        ),
    ]
