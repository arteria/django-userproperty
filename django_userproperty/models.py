from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class UserProperty(models.Model):
    ''' 
    '''
    class Meta:
        verbose_name = 'User Property'
        verbose_name_plural = 'User Properties'

    user = models.ForeignKey(User, related_name='userprop')
    tag = models.CharField('tag', max_length=64)
    switch = models.IntegerField()

    def __str__(self):
        s = "UserProperty for " + self.user.username
        s += " with tag '" + self.tag + "' is set to '" + str(self.switch) + "'."
        return s

@python_2_unicode_compatible
class GlobalProperty(models.Model):
    ''' 
    '''
    class Meta:
        verbose_name='Global Property'
        verbose_name_plural='Global Properties'

    tag = models.CharField('tag', max_length=64, unique=True)
    switch = models.IntegerField()

    def __str__(self):
        return "GlobalProperty with tag '" + self.tag + "' is set to '" + str(self.switch) + "'."
