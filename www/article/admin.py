# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from article.models import Article1, Article2, Article3

##########################################################################
##########################################################################

class ArticleAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {'fields': ('url', 'title', 'content', 'sort', 'sites')},),
		(_('Meta tags'), {'classes': ('collapse',), 'fields': ('description', 'keywords')}),
		#(_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
	)
	
	list_display = ('title', 'url', 'sort')
	list_editable = ('sort',)
	
class Article1Admin(ArticleAdmin):
	def queryset(self, request):
		return super(Article1Admin, self).queryset(request).filter(section=10)
		
class Article2Admin(ArticleAdmin):
	def queryset(self, request):
		return super(Article2Admin, self).queryset(request).filter(section=20)
		
class Article3Admin(ArticleAdmin):
	def queryset(self, request):
		return super(Article3Admin, self).queryset(request).filter(section=30)
	
admin.site.register(Article1, Article1Admin)
admin.site.register(Article2, Article2Admin)
admin.site.register(Article3, Article3Admin)

##########################################################################
##########################################################################