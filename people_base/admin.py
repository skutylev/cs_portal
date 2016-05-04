from django.contrib import admin
from people_base.models import Unit, Position, Person, Degree, ScienceRank
from django_mptt_admin.admin import DjangoMpttAdmin
from django.contrib.admin import DateFieldListFilter
from daterange_filter.filter import DateRangeFilter
from import_export import resources, fields
from import_export.admin import ImportExportMixin
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget, DateWidget
from datetime import date


class UnitAdmin(DjangoMpttAdmin):
    pass

class PositionAdmin(admin.ModelAdmin):
    list_display = ("position", "chief_position" )


class DegreeAdmin(admin.ModelAdmin):
    list_display = ("degree", "short_degree", )

class ScienceRankAdmin(admin.ModelAdmin):
    list_display = ("science_rank", "short_science_rank", )


class PersonResource(resources.ModelResource):

    short_name = fields.Field(column_name='Фамилия И.О.')
    birthday = fields.Field(attribute='birthday', column_name='Дата рождения', widget=DateWidget(format='%d.%m.%Y'))
    age = fields.Field(column_name='Возраст')
    unit = fields.Field(column_name='Подразделение')
    position = fields.Field(column_name='Должность')
    rate = fields.Field(attribute='rate', column_name='Доля ставки')
    degree = fields.Field(attribute='degree', column_name='Ученая степень', widget=ForeignKeyWidget(Degree, field='degree'))
    science_rank = fields.Field(attribute='science_rank', column_name='Ученое звание', widget=ForeignKeyWidget(ScienceRank, field='science_rank'))
    employment_date = fields.Field(attribute='employment_date', column_name='Дата трудоустройства', widget=DateWidget(format='%d.%m.%Y'))
    dismissalt_date = fields.Field(attribute='dismissalt_date', column_name='Срок действия договора', widget=DateWidget(format='%d.%m.%Y'))

    def dehydrate_age(self, person):
        today = date.today()
        if today.year > person.birthday.year:
            return today.year - person.birthday.year
        else:
            return '-'

    def dehydrate_short_name(self, person):
        return '%s %s.%s.' % (person.last_name, person.first_name[0], person.middle_name[0])

    def dehydrate_unit(self, person):
        unit = [unit.unit_name for unit in person.unit.all()]
        units = ','.join(unit)
        return '%s' % units

    def dehydrate_position(self, person):
        position = [position.position for position in person.position.all()]
        positions = ','.join(position)
        return '%s' % positions

    class Meta:
        model = Person
        fields = ('short_name', 'birthday', 'age', 'unit', 'position', 'degree', 'science_rank', 'rate', 'employment_date', 'dismissalt_date',)


class PersonAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display = ('last_name', 'first_name', 'middle_name', 'rate', "email", "employment_date", "dismissalt_date", "publish", )
    list_editable = ("publish", )
    list_filter = ( 'unit',
        ('employment_date', DateRangeFilter),
        ('dismissalt_date', DateRangeFilter),
    )
    filter_horizontal = ("unit", "position",)
    search_fields = ("last_name",)
    resource_class = PersonResource


admin.site.register(Unit, UnitAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(ScienceRank, ScienceRankAdmin)
admin.site.register(Person, PersonAdmin)