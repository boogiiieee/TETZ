# -*- coding: utf-8 -*-

from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from headstuff.models import HeadStuff

################################################################################################################
################################################################################################################
			
class HeadStuffAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('title', 'is_active', 'sort')
	list_filter = ('is_active',)
	list_editable = ('is_active', 'sort')
 
admin.site.register(HeadStuff, HeadStuffAdmin)

################################################################################################################
################################################################################################################