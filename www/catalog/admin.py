# -*- coding: utf-8 -*-

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from catalog.models import Category, Product

##########################################################################
##########################################################################

class CategoryAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('title', 'slug', 'is_active', 'sort')
	list_filter = ('is_active',)
	list_editable = ('is_active', 'sort')
	prepopulated_fields = {"slug": ("title",),}
	fieldsets = (
		(None, {'fields': ('title', 'slug', 'image', 'announcement', 'text', 'is_active', 'sort')},),
		(u'Мета-теги', {'classes': ('collapse',), 'fields': ('description', 'keywords')}),
	)
	
admin.site.register(Category, CategoryAdmin)

##########################################################################
##########################################################################

class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('title', 'slug', 'code', 'category', 'is_active', 'sort')
	list_filter = ('is_active', 'category')
	list_editable = ('is_active', 'sort',)
	prepopulated_fields = {"slug": ("title",),} # заполняем slug по title
	fieldsets = (
		(None, {'fields': ('category', 'title', 'slug', 'code', 'image', 'file', 'text', 'is_active', 'sort')},),
		(u'Мета-теги', {'classes': ('collapse',), 'fields': ('description', 'keywords')}),
	)
	
admin.site.register(Product, ProductAdmin)

##########################################################################
##########################################################################