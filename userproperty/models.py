#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class UserProperty(models.Model):
    '''
    '''
    user = models.ForeignKey(User, related_name='userprop')
    name = models.SlugField('name', max_length=64)
    value = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'User Property'
        verbose_name_plural = 'User Properties'
        unique_together = (("user", "name"),)

    def __str__(self):
        s = "UserProperty for " + self.user.username
        s += " with name '" + self.name + "' is set to '" + str(self.value) + "'."
        return s


@python_2_unicode_compatible
class GlobalProperty(models.Model):
    '''
    '''
    name = models.SlugField('name', max_length=64, unique=True)
    value = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Global Property'
        verbose_name_plural = 'Global Properties'

    def __str__(self):
        return "GlobalProperty with name '" + self.name + "' is set to '" + str(self.value) + "'."
