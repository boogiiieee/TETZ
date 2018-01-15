# -*- coding: utf-8 -*-

from django.db import models
import os

from pytils.translit import slugify
from sorl.thumbnail import ImageField as SorlImageField
from redactor.fields import RedactorField

################################################################################################################
################################################################################################################

class Banner(models.Model):
	def make_upload_path(instance, filename):
		name, extension = os.path.splitext(filename)
		filename = u'%s%s' % (slugify(name), extension)
		return u'upload/banners/%s' % filename.lower()
		
	title = models.CharField(max_length=100, verbose_name=u'заголовок')
	image = SorlImageField(upload_to=make_upload_path, verbose_name=u'изображение', help_text=u'150x150 px размер баннера ')
	description = RedactorField(max_length=1000, verbose_name=u'описание', blank=True)
	is_active = models.BooleanField(verbose_name=u'активно', default=True)
	sort = models.IntegerField(verbose_name=u'порядок', default=0)
	
	def get_title(self): return self.title
	def get_image(self): return self.image
	def get_description(self): return self.description
          
	def __unicode__(self):
		return self.get_title()
     
	class Meta:
		verbose_name = u'баннер'
		verbose_name_plural = u'баннеры'
		ordering = ['sort', '-id']
		
################################################################################################################
################################################################################################################