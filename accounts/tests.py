# Django
from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from accounts.models import Users
from django.utils import timezone


class UserTest(TestCase):
    def setUp(self):
        self.users = Users.objects.create(
            password='abc',
            last_login=timezone.now(),
            is_superuser=True,
            username='Test',
            first_name='Test',
            last_name='Test',
            email='admin@wp.pl',
            is_staff=True,
            is_active=True,
            date_joined=timezone.now(),
            user='Test'
        )

    def test_model(self):
        self.assertEqual(self.users.password, 'abc')
        self.assertEqual(self.users.last_login, self.users.date_joined)