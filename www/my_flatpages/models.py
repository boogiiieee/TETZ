# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.sites.models import Site
import re, os

from redactor.fields import RedactorField

#######################################################################################################################
#######################################################################################################################

class FlatPage(models.Model):
	url 					= models.CharField(max_length=100, db_index=True)
	title 					= models.CharField(max_length=500, verbose_name=u'заголовок', blank=True)
	content 				= RedactorField(u'содержимое', blank=True)
	enable_comments 		= models.BooleanField(verbose_name=u'разрешить комментарии', default=False)
	template_name 			= models.CharField(max_length=70, verbose_name=u'имя шаблона', blank=True,
							help_text	=u"пример: 'flatpages/contact_page.html'. Если не указать, то система будет использовать шаблон по умолчанию 'flatpages/default.html'")
	registration_required   = models.BooleanField(verbose_name=u'требуется регистрация', help_text=u'если отмечено, то только вошедшие в систему пользователи смогут видет страницу')
	sites                   = models.ManyToManyField(Site, verbose_name='сайты')

	description = models.TextField(verbose_name=u'описание', blank=True)
	keywords 	= models.TextField(verbose_name=u'ключевые слова через запятую', blank=True)

	class Meta:
		db_table 			= 'django_flatpage'
		verbose_name 		= u'простая страница'
		verbose_name_plural = u'простые станицы'
		ordering 			= ('title',)
		
	def get_title(self): return self.title
	def get_content(self): return self.content
	def get_description(self): return self.description
	def get_keywords(self): return self.keywords

	def __unicode__(self):
		return u"%s -- %s" % (self.url, self.get_title())

	def get_absolute_url(self):
		return self.url
		
	def get_admin_url(self):
		return u'/admin/my_flatpages/flatpage/%d/' % self.id
		
#######################################################################################################################
#######################################################################################################################
