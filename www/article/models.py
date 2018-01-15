# -*- coding: utf-8 -*-

from django.db import models

from my_flatpages.models import FlatPage

#######################################################################################################################
#######################################################################################################################

class Article(FlatPage):
	SECTION_CHOICES = (
		(10, u'О компании'),
		(20, u'Закупки'),
		(30, u'Акционерам'),
	)

	section = models.IntegerField(choices=SECTION_CHOICES, verbose_name=u'выберите раздел')
	sort	= models.IntegerField(verbose_name=u'порядок', default=0)
	
	class Meta:
		ordering = ['sort', '-id']
		
#######################################################################################################################
#######################################################################################################################

class Article1(Article):
	def save(self, *args, **kwargs):
		self.section = 10
		if not self.template_name:
			self.template_name = 'flatpages/default_10.html'
		super(Article1, self).save(*args, **kwargs)
		
	class Meta: 
		verbose_name = u'статья'
		verbose_name_plural = u'раздел о компании'
		proxy = True
		
class Article2(Article):
	def save(self, *args, **kwargs):
		self.section = 20
		if not self.template_name:
			self.template_name = 'flatpages/default_20.html'
		super(Article2, self).save(*args, **kwargs)
		
	class Meta: 
		verbose_name = u'статья'
		verbose_name_plural = u'раздел закупки'
		proxy = True
		
class Article3(Article):
	def save(self, *args, **kwargs):
		self.section = 30
		if not self.template_name:
			self.template_name = 'flatpages/default_30.html'
		super(Article3, self).save(*args, **kwargs)
		
	class Meta: 
		verbose_name = u'статья'
		verbose_name_plural = u'раздел акционерам'
		proxy = True

#######################################################################################################################
#######################################################################################################################