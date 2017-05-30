# -*- coding: utf-8 -*-
import unittest

from compat import get_user_model
from userproperty import utils


class UserPropertyTestCase(unittest.TestCase):
    def setUp(self):
        User = get_user_model()
        self.user, _ = User.objects.get_or_create(username='tester')

    def test_set_integer_property(self):
        result = utils.set_integer_property(None, name='prop', value=12, anUser=self.user)
        self.assertTrue(result)

    def test_get_integer_property(self):
        pass
        # result = utils.get_integer_property()

    def test_add_property(self):
        result = utils.add_property(None, name='prop', anUser=self.user)
        self.assertTrue(result)

    def test_remove_property(self):
        pass
        # result = utils.remove_property()

    def test_get_all_properties(self):
        pass
        # result = utils.get_all_properties()

    def test_drop_all_properties_for_user(self):
        pass
        # result = utils.drop_all_properties_for_user()

    def test_get_property(self):
        pass
        # result = utils.get_property()

    def test_get_users_with_property(self):
        pass
        # result = utils.get_users_with_property()

    def test_inc_user_property(self):
        pass
        # result = utils.inc_user_property()

    def test_dec_user_property(self):
        pass
        # result = utils.dec_user_property()

    def test_set_global_property(self):
        pass
        # result = utils.set_global_property()

    def test_get_global_property(self):
        pass
        # result = utils.get_global_property()

    def test_get_integer_global_property(self):
        pass
        # result = utils.get_integer_global_property()

    def test_inc_global_property(self):
        pass
        # result = utils.inc_global_property()

    def test_dec_global_property(self):
        pass
        # result = utils.dec_global_property()
