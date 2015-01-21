from django.contrib import admin
from .models import UserProperty, GlobalProperty


class UserPropertyAdmin(admin.ModelAdmin):
    list_display = ('user', 'tag',)
    list_filter = ('user', 'tag',)

admin.site.register(UserProperty, UserPropertyAdmin)


class GlobalPropertyAdmin(admin.ModelAdmin):
    list_display = ('tag', 'switch',)
    list_filter = ('tag', 'switch',)

admin.site.register(GlobalProperty, GlobalPropertyAdmin)
