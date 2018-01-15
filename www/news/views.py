# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.sitemaps import Sitemap
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from news.conf import settings as conf
from news.models import NewsArticle


##########################################################################
##########################################################################

#Для карты сайта
class NewsSitemap(Sitemap):
	def items(self):
		return NewsArticle.objects.filter(is_active=True)
		
	def location(self, obj):
		return obj.get_item_url()
		
##########################################################################
##########################################################################

class NewsList(ListView):
	paginate_by = conf.PAGINATE_BY
	template_name = 'news/news.html'
	context_object_name = 'news_list'
	
	def get_queryset(self):
		return NewsArticle.objects.filter(is_active=True)
		
	def get_context_data(self, **kwargs):
		context = super(NewsList, self).get_context_data(**kwargs)
		context.update({'active':'news',})
		return context
	
##########################################################################
##########################################################################

class NewsFull(NewsList):
	template_name = 'news/item.html'
	slug_url_kwarg = 'slug'
	
	def get_slug(self):
		return self.kwargs.get(self.slug_url_kwarg, None)

	def get_context_data(self, **kwargs):
		context = super(NewsFull, self).get_context_data(**kwargs)
		item = get_object_or_404(NewsArticle, slug=self.get_slug(), is_active=True)
		context.update({'item_new':item, 'active':'news'})
		return context
	
##########################################################################
##########################################################################