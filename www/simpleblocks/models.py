# -*- coding: utf-8 -*-

from django.db import models

from redactor.fields import RedactorField

################################################################################################################
################################################################################################################

class Block(models.Model):
	title = models.CharField(max_length=200, verbose_name=u'заголовок')
	text = RedactorField(max_length=1000, verbose_name=u'текст')
	
	def get_title(self): return self.title
	def get_text(self): return self.text
	
	def __unicode__(self):
		return self.get_title()
		
	class Meta: 
		verbose_name = u'модуль' 
		verbose_name_plural = u'текстовые модули'
		ordering = ['title']
		
################################################################################################################
################################################################################################################