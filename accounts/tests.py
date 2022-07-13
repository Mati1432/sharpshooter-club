# Django
from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from accounts.models import Users
from django.utils import timezone


class UserModelTest(TestCase):
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

    def test_simple_user_creation(self):
        users = self.users
        self.assertIsNotNone(users)
        self.assertIsInstance(users, Users)
        self.assertEqual(users.first_name, 'Test')
        self.assertFalse(users.user_permissions.exists())
        self.assertFalse(users.groups.exists())

    def test_simple_user_update(self):
        users = self.users
        users.first_name = 'Test2'
        users.save()
        self.assertEqual(users.first_name, 'Test2')

    def test_simple_user_delete(self):
        Users.objects.all().delete()
        self.assertFalse(Users.objects.exists())

    def test_simple_users_retrieving(self):
        users_get = Users.objects.get(id=self.users.id)
        self.assertEqual(self.users.id, users_get.id)
