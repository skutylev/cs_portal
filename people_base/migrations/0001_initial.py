# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('degree', models.CharField(max_length=50, verbose_name='Ученая степень')),
                ('short_degree', models.CharField(max_length=6, verbose_name='Сокращение')),
            ],
            options={
                'verbose_name_plural': 'Ученые степени',
                'verbose_name': 'Ученая степень',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('birthday', models.DateField(blank=True, verbose_name='Дата рождения', default='31.12.2099')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('rate', models.FloatField(verbose_name='Доля ставки', default='1.0')),
                ('employment_date', models.DateField(blank=True, verbose_name='Дата устройства')),
                ('dismissalt_date', models.DateField(blank=True, verbose_name='Дата увольнения', default='31.12.2099')),
                ('publish', models.BooleanField(verbose_name='Опубликовано', default=False)),
                ('degree', models.ForeignKey(to='people_base.Degree', verbose_name='Ученая степень', default='3')),
            ],
            options={
                'verbose_name_plural': 'Сотрудники',
                'verbose_name': 'Сотрудник',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
                ('chief_position', models.CharField(blank=True, max_length=50, verbose_name='Начальник')),
            ],
            options={
                'verbose_name_plural': 'Должности',
                'verbose_name': 'Должность',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='ScienceRank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('science_rank', models.CharField(max_length=50, verbose_name='Ученое звание')),
                ('short_science_rank', models.CharField(max_length=6, verbose_name='Сокращение')),
            ],
            options={
                'verbose_name_plural': 'Ученые звания',
                'verbose_name': 'Ученое звание',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('unit_name', models.CharField(max_length=100, verbose_name='Подразделение')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', models.ForeignKey(blank=True, to='people_base.Unit', verbose_name='Родитель', null=True, related_name='child')),
            ],
            options={
                'verbose_name_plural': 'Подразделения',
                'verbose_name': 'Подразделение',
                'ordering': ['unit_name'],
            },
        ),
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.ManyToManyField(verbose_name='Должность', to='people_base.Position'),
        ),
        migrations.AddField(
            model_name='person',
            name='science_rank',
            field=models.ForeignKey(to='people_base.ScienceRank', verbose_name='Ученое звание', default='3'),
        ),
        migrations.AddField(
            model_name='person',
            name='unit',
            field=models.ManyToManyField(verbose_name='Подразделение', to='people_base.Unit'),
        ),
    ]
