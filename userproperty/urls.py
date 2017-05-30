# -*- coding: utf-8 -*-
from django.conf.urls import url

from userproperty import views


urlpatterns = [
    # user properties
    url(r'^get-uproperty/$',
        views.get_user_property,
        name='get_user_property', ),
    url(r'^set-uproperty/$',
        views.set_user_property,
        name='set_user_property', ),

    # global properties
    url(r'^get-gproperty/$',
        views.get_global_property,
        name='get_global_property', ),
    url(r'^set-gproperty/$',
        views.set_global_property,
        name='set_global_property', ),
]
