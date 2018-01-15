# -*- coding: utf-8 -*-

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from banners.models import Banner

################################################################################################################
################################################################################################################
			
class BannerAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('title', 'is_active', 'sort')
	list_filter = ('is_active',)
	list_editable = ('is_active', 'sort')
 
admin.site.register(Banner, BannerAdmin)

################################################################################################################
################################################################################################################