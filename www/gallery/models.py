# -*- coding: utf-8 -*-

from django.db import models
import os

from pytils.translit import slugify
from sorl.thumbnail import ImageField as SorlImageField

################################################################################################################
################################################################################################################

class Gallery(models.Model):
	def make_upload_path(instance, filename):
		name, extension = os.path.splitext(filename)
		filename = u'%s%s' % (slugify(name), extension)
		return u'upload/gallery/%s' % filename.lower()
		
	title = models.CharField(max_length=100, verbose_name=u'Ф.И.О.')
	image = SorlImageField(upload_to=make_upload_path, verbose_name=u'изображение')# добавить help_text=u'260x240 px размер фото' с размерами исходя из дизайна
	description = models.TextField(max_length=1000, verbose_name=u'краткое описание', blank=True)
	is_active = models.BooleanField(verbose_name=u'активно', default=True)
	sort = models.IntegerField(verbose_name=u'порядок', default=0)
	
	def get_title(self): return self.title
	def get_image(self): return self.image
	def get_description(self): return self.description
          
	def __unicode__(self):
		return self.get_title()
     
	class Meta:
		verbose_name = u'фото'
		verbose_name_plural = u'галлерея'
		ordering = ['sort', 'id']
		
################################################################################################################
################################################################################################################