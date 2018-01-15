# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import FlatPageSitemap
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from news.views import NewsSitemap
from catalog.views import CategorySitemap, ProductSitemap

sitemaps = {
	'flatpages': FlatPageSitemap,
	'news': NewsSitemap,
	'catalog':CategorySitemap,
	'product':ProductSitemap
}

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^admin_tools/', include('admin_tools.urls')),
	
	url(r'^redactor/', include('redactor.urls')),
	url(r'^robots\.txt$', include('robots.urls')),
	
	url(r'^news/', include('news.urls')),
	url(r'^catalog/', include('catalog.urls')),
	
	url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),	
	
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), 
)
