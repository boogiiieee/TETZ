# -*- coding: utf-8 -*-

from django.conf.urls import *

from news.views import NewsFull, NewsList

urlpatterns = patterns('news.views',
	url(r'^$', NewsList.as_view(), name='news_url'),	
	url(r'^(?P<slug>[-_\w]+)/$', NewsFull.as_view(), name='news_item_url'),
)