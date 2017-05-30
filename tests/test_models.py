# -*- coding: utf-8 -*-
import unittest

from compat import get_user_model
from userproperty import models


class UserPropertyTestCase(unittest.TestCase):
    def setUp(self):
        User = get_user_model()
        self.user, _ = User.objects.get_or_create(username='tester')

    def test_userproperty_create(self):
        prop = models.UserProperty(
            user=self.user,
            name='prop',
            value=10,
        )
        prop.save()
        prop.refresh_from_db()
        self.assertEquals(prop.user, self.user)
        self.assertEquals(prop.name, 'prop')
        self.assertEquals(prop.value, '10')


class GlobalPropertyTestCase(unittest.TestCase):
    def test_create(self):
        prop = models.GlobalProperty(
            name='prop',
            value=10,
        )
        prop.save()
        prop.refresh_from_db()
        self.assertEquals(prop.name, 'prop')
        self.assertEquals(prop.value, '10')
