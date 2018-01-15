# -*- coding: utf-8 -*-

import os
def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

SECRET_KEY = 'k6!rr7e=pvp^6c29f8hcfnmc%a$_=q2z*1km(_-ucf^c3_1@&3'	

TEST = False
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('GVA', 'GladkiyVA@gmail.com'),
	('POA', 'poa.webaspect@gmail.com'),
	('KVS', 'korsvs@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'tetz',                     
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['127.0.0.1:8000', 'localhost']

TIME_ZONE = 'Asia/Novosibirsk'
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = rel('media')
MEDIA_URL = '/media/'

STATIC_ROOT = rel('static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	# Uncomment the next line for simple clickjacking protection:
	# 'django.middleware.clickjacking.XFrameOptionsMiddleware',

	'my_flatpages.middleware.FlatpageFallbackMiddleware',
	'configuration.middleware.ConfigurationMiddleware',
)

ROOT_URLCONF = 'www.urls'

#WSGI_APPLICATION = 'www.wsgi.application'

TEMPLATE_DIRS = (
	rel('..', 'admin_tools_ru', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
	'admin_tools',
	'admin_tools.theming',
	'admin_tools.menu',
	'admin_tools.dashboard',

	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	'django.contrib.sitemaps',

	'tetz',
	'front_admin',
	'my_flatpages',
	'configuration',
	'map2gis',
	'simpleblocks',
	'copyright',
	'banners',
	'headstuff',
	'news',
	'paginator',
	'catalog',
	'article',

	'redactor',
	'sorl.thumbnail',
	'annoying',
	'django_cleanup',
	'robots',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

REDACTOR_OPTIONS = {'lang':'ru', 'tidyHtml':True, 'removeEmptyTags':False, 'wym': True, 'convertDivs': False, 'fullpage': False, 'fullscreen':False,  'paragraphy': True,}

PAGINATE_BY = 10
NEWS_PAGINATE_BY = PAGINATE_BY

ROBOTS_SITEMAP_URLS = ['http://127.0.0.1:8000/sitemap.xml']
ROBOTS_SITEMAP_HOST = '127.0.0.1:8000'

ADMIN_TOOLS_MENU = 'www.dashboard.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'www.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'www.dashboard.CustomAppIndexDashboard'
ADMIN_TOOLS_THEMING_CSS = 'admin_tools/css/theming_tomu.css'