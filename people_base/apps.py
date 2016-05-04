from django.apps import AppConfig


class PeopleBaseConfig(AppConfig):
    name = 'people_base'
    verbose_name = 'Штатное расписание'


class CMSConfig(AppConfig):
    name = 'cms'
    verbose_name = 'Управление CMS'
