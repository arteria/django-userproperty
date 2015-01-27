#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('userproperty.views',
    # user properties
    url(r'^get-uproperty/$',
        view='get_user_property',
        name='get_user_property',
    ),
    url(r'^set-uproperty/$',
        view='set_user_property',
        name='set_user_property',
    ),

    # global properties
    url(r'^get-gproperty/$',
        view='get_global_property',
        name='get_global_property',
    ),
    url(r'^set-gproperty/$',
        view='set_global_property',
        name='set_global_property',
    ),
)
