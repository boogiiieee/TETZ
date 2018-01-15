# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.sitemaps import Sitemap
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from annoying.functions import get_object_or_None

from catalog.models import Category, Product

##########################################################################
##########################################################################

#Для карты сайта
class CategorySitemap(Sitemap):
	def items(self):
		return Category.objects.filter(is_active=True)
		
	def location(self, obj):
		return obj.get_category_url()
		
class ProductSitemap(Sitemap):
	def items(self):
		return Product.objects.filter(is_active=True)
		
	def location(self, obj):
		return obj.get_absolute_url()
		
##########################################################################
##########################################################################

class CatalogList(ListView):
	template_name = 'catalog/catalog.html'
	context_object_name = 'category_list'

	def get_queryset(self):
		return Category.objects.filter(is_active=True)
		
	def get_context_data(self, **kwargs):
		context = super(CatalogList, self).get_context_data(**kwargs)
		context.update({'active':'category',})
		
		return context
	
##########################################################################
##########################################################################

class ProductList(ListView):
	template_name = 'catalog/category.html'
	context_object_name = 'product_list'
	slug_url_kwarg = 'slug'
	
	def get_slug(self):
		return self.kwargs.get(self.slug_url_kwarg, None)

	def get_queryset(self):
		slug = self.get_slug()
		return Product.objects.filter(category__slug=slug, is_active=True)
		
	def get_context_data(self, **kwargs):
		context = super(ProductList, self).get_context_data(**kwargs)
		
		slug = self.get_slug()
		category = get_object_or_None(Category, slug=slug, is_active=True)
		context.update({'category':category, 'active':'category',})
		
		return context
	
##########################################################################
##########################################################################

class ProductItem(DetailView):
	template_name = 'catalog/product.html'
	context_object_name='product'
	
	def get_queryset(self):
		return Product.objects.filter(is_active=True)
		
	def get_context_data(self, **kwargs):
		context = super(ProductItem, self).get_context_data(**kwargs)
		context.update({'active':'category',})
		
		return context
	
##########################################################################
##########################################################################