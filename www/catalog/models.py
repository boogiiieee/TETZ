# -*- coding: utf-8 -*-

from django.db import models
import re, os

from pytils.translit import slugify
from redactor.fields import RedactorField
from sorl.thumbnail import ImageField as SorlImageField

##########################################################################
##########################################################################

class Category (models.Model):
	def make_upload_path(instance, filename):
		name, extension = os.path.splitext(filename)
		filename = u'%s%s' % (slugify(name), extension)
		return u'upload/catalog/category/%s' % filename.lower()
		
	title		= models.CharField(max_length=100, verbose_name=u'название')
	image		= SorlImageField(upload_to=make_upload_path, verbose_name=u'изображение', blank=True, null=True)
	announcement= models.TextField(max_length=500, verbose_name=u'анонс')
	text		= RedactorField(max_length=100000, verbose_name=u'текст', blank=True, null=True)
	slug 		= models.SlugField(max_length=500, verbose_name=u'псевдоним', unique=True)
	is_active 	= models.BooleanField(verbose_name=u'активно', default=True)
	sort 		= models.IntegerField(verbose_name=u'порядок', default=0)
	
	description = models.TextField(u'описание', blank=True)
	keywords = models.TextField(u'ключевые слова через запятую', blank=True)
	
	def get_title(self): return self.title
	def get_image(self): return self.image
	def get_announcement(self): return self.announcement
	def get_text(self): return self.text
	
	def __unicode__(self):
		return u'%s' % self.get_title()
		
	@models.permalink
	def get_absolute_url(self):
		return ('catalog_url', (), {})
		
	@models.permalink
	def get_category_url(self):
		return ('category_url', (), {'slug':self.slug})
		
	def get_admin_url(self):
		return u'/admin/catalog/category/%d/' % self.id
		
	def get_admin_product_list_url(self):
		return u'/admin/catalog/product/?category__id__exact=%d' % self.id
		
	class Meta: 
		verbose_name = u'категория'
		verbose_name_plural = u'категории'
		ordering = ['sort', '-id']
		
##########################################################################
##########################################################################

class Product (models.Model):
	def make_upload_path(instance, filename):
		name, extension = os.path.splitext(filename)
		filename = u'%s%s' % (slugify(name), extension)
		return u'upload/catalog/product/%s' % filename.lower()
	
	category	= models.ForeignKey(Category, verbose_name=u'категория')	
	title		= models.CharField(max_length=100, verbose_name=u'название')
	slug 		= models.SlugField(max_length=500, verbose_name=u'псевдоним', unique=True)
	code		= models.CharField(max_length=100, verbose_name=u'номер в каталоге', blank=True)
	text		= RedactorField(max_length=100000, verbose_name=u'текст')
	image		= SorlImageField(upload_to=make_upload_path, verbose_name=u'изображение', blank=True, null=True)
	file		= models.FileField(upload_to=make_upload_path, verbose_name=u'файл', blank=True)
	is_active 	= models.BooleanField(verbose_name=u'активно', default=True)
	sort 		= models.IntegerField(verbose_name=u'порядок', default=0)
	
	description = models.TextField(u'описание', blank=True)
	keywords = models.TextField(u'ключевые слова через запятую', blank=True)
	
	def get_title(self): return self.title
	def get_image(self): return self.image
	def get_code(self): return self.code
	def get_text(self): return self.text
	def get_file(self): return self.file
	
	def __unicode__(self):
		return u'%s' % self.get_title()
		
	@models.permalink
	def get_absolute_url (self):
		return ('product_url', (), {'slug_category':self.category.slug, 'slug':self.slug})
		
	def get_admin_url(self):
		return u'/admin/catalog/product/%d/' % self.id
	
	class Meta: 
		verbose_name = u'товар'
		verbose_name_plural = u'продукция'
		ordering = ['sort', '-id']
	
##########################################################################
##########################################################################