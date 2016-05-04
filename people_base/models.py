from django.db import models
from hashlib import md5
from os import path as op
from time import time
from ckeditor.fields import RichTextField
import mptt


###########################
# Добавляем модели данных #
###########################


# Справочник подразделений, с шифрами и иерархией
class Unit(models.Model):
    unit_name = models.CharField(max_length=100, verbose_name='Подразделение')
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name='Родитель', related_name='child')

    def __str__(self):
        return self.unit_name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ['unit_name']
mptt.register(Unit,)

# Справочник должностей, с начальниками и подчиненными
class Position(models.Model):
    position = models.CharField(max_length=50, verbose_name='Должность')
    chief_position = models.CharField(max_length=50, verbose_name='Начальник', blank=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['position']


# Ученые степени
class Degree(models.Model):
    degree = models.CharField(max_length=50, verbose_name='Ученая степень')
    short_degree = models.CharField(max_length=6, verbose_name='Сокращение')

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name = 'Ученая степень'
        verbose_name_plural = 'Ученые степени'

# Ученые звания
class ScienceRank(models.Model):
    science_rank = models.CharField(max_length=50, verbose_name='Ученое звание')
    short_science_rank = models.CharField(max_length=6, verbose_name='Сокращение')

    def __str__(self):
        return self.science_rank

    class Meta:
        verbose_name = 'Ученое звание'
        verbose_name_plural = 'Ученые звания'

class Person(models.Model):
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    middle_name = models.CharField(max_length=30, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, default='31.12.2099')
    email = models.EmailField(verbose_name='Email',  blank=True)
    unit = models.ManyToManyField(Unit, verbose_name='Подразделение')
    position = models.ManyToManyField(Position, verbose_name='Должность')
    degree = models.ForeignKey(Degree, verbose_name='Ученая степень', default='3')
    science_rank = models.ForeignKey(ScienceRank, verbose_name='Ученое звание', default='3')
    rate = models.FloatField(verbose_name='Доля ставки', default='1.0')
    employment_date = models.DateField(verbose_name='Дата устройства', blank=True)
    dismissalt_date = models.DateField(verbose_name='Дата увольнения', blank=True, default='31.12.2099')
    publish = models.BooleanField(default=False, verbose_name='Опубликовано')
    comment = RichTextField(max_length=800, verbose_name='Комментарий', blank=True)


    def __str__(self):
        return u'%s %s.%s.' % (self.last_name, self.first_name[:1], self.middle_name[:1])

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['last_name']