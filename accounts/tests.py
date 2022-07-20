"""Tests file."""
# Standard Library
import secrets
import string

# Django
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone

# Project
from accounts.forms import SignUpForm
from accounts.models import AchievementCompetition
from accounts.models import AchievementIndividual
from accounts.models import License
from accounts.models import Users


class UserModelTest(TestCase):  # noqa D101
    def setUp(self):  # noqa D102
        self.randomize_password = ''.join((secrets.choice(
            string.ascii_letters + string.digits)
            for i in range(20)),
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

    def test_simple_user_creation(self):  # noqa D102
        users = self.users
        self.assertIsNotNone(users)
        self.assertIsInstance(users, Users)
        self.assertEqual(users.first_name, 'Name')
        self.assertFalse(users.user_permissions.exists())
        self.assertFalse(users.groups.exists())

    def test_simple_user_update(self):  # noqa D102
        users = self.users
        users.first_name = 'Name2'
        users.save()
        self.assertEqual(users.first_name, 'Name2')

    def test_simple_user_delete(self):  # noqa D102
        Users.objects.all().delete()
        self.assertFalse(Users.objects.exists())

    def test_simple_users_retrieving(self):  # noqa D102
        users_get = Users.objects.get(id=self.users.id)
        self.assertEqual(self.users.id, users_get.id)


class SignUpFormTest(TestCase):  # noqa D101
    def setUp(self):  # noqa D102
        self.randomize_password = ''.join((secrets.choice(
            string.ascii_letters + string.digits)
            for i in range(20)),
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

    def test_validate_form(self):  # noqa D102
        form = SignUpForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_different_password(self):  # noqa D102
        self.form_data['password2'] = self.randomize_password + self.randomize_password
        form = SignUpForm(data=self.form_data)
        self.assertFalse(form.is_valid())


class AchievementIndividualModelTest(TestCase):  # noqa D101
    def setUp(self):  # noqa D102
        user_model_test = UserModelTest()
        user_model_test.setUp()
        self.achievement = AchievementIndividual.objects.create(
            name='Name',
            date=timezone.now(),
            score=47,
            users_achievement_individual=user_model_test.users,
        )

    def test_achievement_individual_model(self):  # noqa D102
        achievement = AchievementIndividual.objects.get(id=1)
        self.assertEqual(achievement.name, 'Name')
        self.assertEqual(achievement.date, timezone.now().date())
        self.assertIsNotNone(achievement)
        self.assertTrue(AchievementIndividual.objects.filter(name='Name').exists())
        self.assertTrue(AchievementIndividual.objects.filter(score=47).exists())
        self.assertTrue(AchievementIndividual.objects.filter(
            users_achievement_individual=achievement.users_achievement_individual.id).exists())

    def test_simple_achivement_update(self):  # noqa D102
        achievement = self.achievement
        achievement.name = 'Name2'
        achievement.date = timezone.now().date()
        achievement.score = 49
        achievement.save()

        self.assertEqual(achievement.name, 'Name2')
        self.assertEqual(achievement.date, timezone.now().date())
        self.assertEqual(achievement.score, 49)
        self.assertFalse(AchievementIndividual.objects.filter(name='Name').exists())

    def test_simple_achivement_delete(self):  # noqa D102
        AchievementIndividual.objects.all().delete()
        self.assertFalse(AchievementIndividual.objects.exists())


class AchievementCompetitionModelTest(TestCase):  # noqa D101
    def setUp(self):  # noqa D102
        user_model_test = UserModelTest()
        user_model_test.setUp()

        self.achievement_competition = AchievementCompetition.objects.create(
            name='Name Competition',
            date=timezone.now(),
            score=52,
            user_achievement_competition=user_model_test.users,
        )

    def test_achievement_competition_model(self):  # noqa D102
        achievement = AchievementCompetition.objects.get(id=1)
        self.assertEqual(achievement.name, 'Name Competition')
        self.assertIsNotNone(achievement)
        self.assertEqual(achievement.date, timezone.now().date())
        self.assertTrue(AchievementCompetition.objects.filter(name='Name Competition').exists())
        self.assertTrue(AchievementCompetition.objects.filter(score=52).exists())
        self.assertTrue(AchievementCompetition.objects.filter(
            user_achievement_competition=achievement.user_achievement_competition.id).exists())

    def test_simple_competition_update(self):  # noqa D102
        achievement = self.achievement_competition
        achievement.name = 'Name2'
        achievement.date = timezone.now().date()
        achievement.score = 53
        achievement.save()

        self.assertEqual(achievement.name, 'Name2')
        self.assertEqual(achievement.date, timezone.now().date())
        self.assertEqual(achievement.score, 53)
        self.assertFalse(AchievementCompetition.objects.filter(name='Name Competition').exists())

    def test_simple_competition_delete(self):  # noqa D102
        AchievementCompetition.objects.all().delete()
        self.assertFalse(AchievementCompetition.objects.exists())


class LicenseModelTest(TestCase):  # noqa D101
    def setUp(self):  # noqa D102
        user_model_test = UserModelTest()
        user_model_test.setUp()
        self.license = License.objects.create(
            license_is_active=False,
            date=timezone.now().date(),
            license_type='Rifle',
            user_license=user_model_test.users,
        )

    def test_simple_license_model(self):  # noqa D102
        license_user = self.license
        self.assertEqual(license_user.license_is_active, False)
        self.assertEqual(license_user.date, timezone.now().date())
        self.assertIsNotNone(license_user)
        self.assertTrue(License.objects.all().exists())
        self.assertTrue(License.objects.filter(license_type='Rifle').exists())
        self.assertTrue(License.objects.filter(user_license=license_user.user_license.id).exists())

    def test_simple_license_update(self):  # noqa D102
        license_user = self.license
        license_user.license_is_active = True
        license_user.license_type = 'Pistol'
        license_user.save()

        self.assertEqual(license_user.license_is_active, True)
        self.assertEqual(license_user.date, timezone.now().date())
        self.assertEqual(license_user.license_type, 'Pistol')
        self.assertFalse(License.objects.filter(license_type='Rifle').exists())

    def test_simple_license_delete(self):  # noqa D102
        license_user = self.license
        license_user.delete()
        self.assertFalse(License.objects.all().exists())
