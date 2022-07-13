# Django
import secrets
import string

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from accounts.forms import SignUpForm
from accounts.models import Users
from django.utils import timezone


class UserModelTest(TestCase):
    def setUp(self):
        self.randomize_password = ''.join((secrets.choice(
            string.ascii_letters + string.digits)
            for i in range(20))
        )
        upload_file = open(r'C:\Users\Mateusz\Desktop\test.jpg', 'rb')
        self.users = Users.objects.create(
            password=self.randomize_password,
            last_login=timezone.now(),
            is_superuser=True,
            username='Test',
            first_name='Name',
            last_name='Last Name',
            email='test@test.com',
            is_staff=True,
            is_active=True,
            date_joined=timezone.now(),
            city='City',
            pesel='12345678901',
            postal_code='00-000',
            street='Street',
            house_number='00',
            phone='+00 000000000',
            photo=SimpleUploadedFile(upload_file.name, upload_file.read()),
            club='Club',
            birth_date='2022-07-13',

        )

    def test_simple_user_creation(self):
        users = self.users
        self.assertIsNotNone(users)
        self.assertIsInstance(users, Users)
        self.assertEqual(users.first_name, 'Name')
        self.assertFalse(users.user_permissions.exists())
        self.assertFalse(users.groups.exists())

    def test_simple_user_update(self):
        users = self.users
        users.first_name = 'Name2'
        users.save()
        self.assertEqual(users.first_name, 'Name2')

    def test_simple_user_delete(self):
        Users.objects.all().delete()
        self.assertFalse(Users.objects.exists())

    def test_simple_users_retrieving(self):
        users_get = Users.objects.get(id=self.users.id)
        self.assertEqual(self.users.id, users_get.id)


class SignUpFormTest(TestCase):
    def setUp(self):
        self.randomize_password = ''.join((secrets.choice(
            string.ascii_letters + string.digits)
            for i in range(20))
        )
        upload_file = open(r'C:\Users\Mateusz\Desktop\test.jpg', 'rb')

        self.form_data = {
            'first_name': 'Name',
            'last_name': 'Last_name',
            'email': 'test@test.com',
            'city': 'City',
            'pesel': '12345678901',
            'postal_code': '00-000',
            'street': 'Street',
            'house_number': '00',
            'phone': '+00 000000000',
            'photo': SimpleUploadedFile(upload_file.name, upload_file.read()),
            'club': 'Club',
            'date_brith': '2022-07-13',
            'password1': self.randomize_password,
            'password2': self.randomize_password,
        }

    def test_validate_form(self):
        form = SignUpForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_different_password(self):
        self.form_data['password2'] = self.randomize_password + self.randomize_password
        form = SignUpForm(data=self.form_data)
        self.assertFalse(form.is_valid())
