"""
Django settings for untitled3 project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import abspath, basename, dirname, join, normpath
gettext = lambda s: s

SITE_ID = 1
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-7njamr@esnjf$-oo1h+!1u7j1ywh=qotyxzgup4@g1fn%h6#h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    # 'suit',
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'people_base',
    'ckeditor',
    'django_mptt_admin',
    'haystack',
    'daterange_filter',
    'import_export',
    'djangocms_text_ckeditor',
    'cms',
    'schedule',
    'treebeard',
    'menus',
    'sekizai',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'djangocms_link',
    'djangocms_snippet',
    'report_builder',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)


ROOT_URLCONF = 'untitled3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR,  'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'untitled3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('ru', 'Russian'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = normpath(join(BASE_DIR, 'static', 'collected'))

STATICFILES_DIRS = (
    normpath(join(BASE_DIR, 'static')),
)
CKEDITOR_UPLOAD_PATH = (
    os.path.join(BASE_DIR,  'uploads'),
)

AUTHENTICATION_BACKENDS = (
    # 'django_auth_ldap3_ad.auth.LDAP3ADBackend',
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
)
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://178.62.255.252:9266/',
        'INDEX_NAME': 'haystack',
    },
}


# SUIT_CONFIG = {
#     # header
#     'ADMIN_NAME': 'ФКН ВШЭ',
#     'HEADER_DATE_FORMAT': 'l, j E Y',
#     'HEADER_TIME_FORMAT': 'H:i',
# }

# LDAP_SERVERS = [
#     # {
#     #     'host': '192.168.0.13',
#     #     'port': 389,
#     #     'use_ssl': False,
#     # },
#     {
#         'host': '172.16.1.2',
#         'port': 389,
#         'use_ssl': False,
#     },
# ]
#
# # LDAP_BIND_USER = "CN=Кутылев С.А.,OU=Administrators,OU=MITHT,DC=vuz,DC=mitht,DC=ru"
# LDAP_BIND_USER = "CN=Кутылев С.А.,OU=Administrators,OU=MITHT,DC=vuz,DC=mitht,DC=ru"
# LDAP_BIND_PWD = "ReNsKtDcThUtQ1988"
# LDAP_SEARCH_BASE = "OU=Administrators,OU=MITHT,DC=vuz,DC=mitht,DC=ru"
# LDAP_USER_SEARCH_FILTER = "(&(sAMAccountName=%s)(objectClass=user))"
# LDAP_ATTRIBUTES_MAP = {
#     'username': 'sAMAccountName',
#     'first_name': 'givenName',
#     'last_name': 'sn',
#     'email': 'mail',
# }

CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
)