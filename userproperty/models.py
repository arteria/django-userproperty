# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from compat import user_model_label as USER_MODEL  # NOQA


@python_2_unicode_compatible
class UserProperty(models.Model):
    """
    """
    user = models.ForeignKey(USER_MODEL, verbose_name=_('user'), related_name="user_properties")
    name = models.SlugField(_('name'), max_length=64)
    value = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'User Property'
        verbose_name_plural = 'User Properties'
        unique_together = (("user", "name"),)

    def __str__(self):
        return u"UserProperty for {} with name '{}' is set to '{}'".format(self.user, self.name, self.value)


@python_2_unicode_compatible
class GlobalProperty(models.Model):
    """
    """
    name = models.SlugField(_('name'), max_length=64, unique=True)
    value = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Global Property'
        verbose_name_plural = 'Global Properties'

    def __str__(self):
        return "GlobalProperty with name '{}' is set to '{}'".format(self.name, self.value)
