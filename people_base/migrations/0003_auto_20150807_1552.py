# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people_base', '0002_auto_20150807_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='rate',
            field=models.FloatField(default='1.0', verbose_name='Доля ставки'),
        ),
    ]
