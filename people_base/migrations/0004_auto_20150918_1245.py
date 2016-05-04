# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people_base', '0003_auto_20150807_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='comment',
            field=ckeditor.fields.RichTextField(max_length=800, verbose_name='Комментарий', default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email', blank=True),
        ),
    ]
