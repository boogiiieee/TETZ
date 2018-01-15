# -*- coding: utf-8 -*-

from django.conf.urls import *

from catalog.views import CatalogList, ProductList, ProductItem

urlpatterns = patterns('catalog.views',
	url(r'^$', CatalogList.as_view(), name='catalog_url'),	
	url(r'^(?P<slug>[-_\w]+)/$', ProductList.as_view(), name='category_url'),
	url(r'^(?P<slug_category>[-_\w]+)/(?P<slug>[-_\w]+)/$', ProductItem.as_view(), name='product_url'),
)