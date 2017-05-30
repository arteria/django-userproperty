# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^properties/', include('userproperty.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
