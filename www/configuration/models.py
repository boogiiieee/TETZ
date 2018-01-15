# -*- coding: utf-8 -*-

from django.db import models

from map2gis.django_2gis_widget import LocationField

#######################################################################################################################
#######################################################################################################################

#Настройки
class ConfigModel(models.Model):
		
	title = models.CharField(max_length=100, verbose_name=u'название сайта', default=u'Название сайта')
	
	is_active_map = models.BooleanField(verbose_name=u'показывать карту', default=True)
	address = LocationField(verbose_name=u'адрес', blank=True, null=True)
	
	def __unicode__(self):
		return u'настройки'
		
	class Meta: 
		verbose_name = u'настройки' 
		verbose_name_plural = u'настройки'

#######################################################################################################################
#######################################################################################################################