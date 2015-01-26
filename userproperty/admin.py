#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from userproperty.models import UserProperty, GlobalProperty


class UserPropertyAdmin(admin.ModelAdmin):
    list_display = ('user', 'name',)
    list_filter = ('user', 'name',)

admin.site.register(UserProperty, UserPropertyAdmin)


class GlobalPropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'value',)
    list_filter = ('name', 'value',)

admin.site.register(GlobalProperty, GlobalPropertyAdmin)
