# -*- coding: utf-8 -*-

from django.contrib import admin
from userproperty.models import UserProperty, GlobalProperty


class UserPropertyAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'value',)
    raw_id_fields = ('user',)
    search_fields = ['name', 'value']


class GlobalPropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)
    search_fields = ['name', 'value']


admin.site.register(UserProperty, UserPropertyAdmin)
admin.site.register(GlobalProperty, GlobalPropertyAdmin)
