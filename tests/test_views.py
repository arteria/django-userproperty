# -*- coding: utf-8 -*-
from django.test import Client
from django.test import TestCase

from compat import get_user_model
from userproperty import views


class ViewsTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
        self.client = Client()
        self.client.login(username='foo', password='bar')

        user = User.objects.create_user('foo_staff', 'myemail@test.com', 'bar', is_staff=True)
        self.staff_client = Client()
        self.staff_client.login(username='foo_staff', password='bar')

    def test_get_user_property(self):
        response = self.client.get('/properties/get-uproperty/?name=prop&default=12')

    def test_set_user_property(self):
        response = self.client.get('/properties/set-uproperty/?name=prop&value=12')

    def test_get_global_property(self):
        response = self.staff_client.get('/properties/get-gproperty/?name=prop&default=12')

    def test_set_global_property(self):
        response = self.staff_client.get('/properties/set-gproperty/?name=prop&value=12')
