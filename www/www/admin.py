# -*- coding: utf-8 -*-

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

##########################################################################
##########################################################################


UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

##########################################################################
##########################################################################