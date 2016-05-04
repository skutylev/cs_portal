# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people_base', '0004_auto_20150918_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='comment',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Комментарий', max_length=800),
        ),
    ]
