"""Models file."""
# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from .consts import license_type_consts


class Users(AbstractUser):  # noqa: D101
    pesel = models.CharField(max_length=11)
    birth_date = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=45)
    postal_code = models.CharField(max_length=7)
    street = models.CharField(max_length=45)
    house_number = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='Images/', null=True, blank=True)
    club = models.CharField(max_length=20, blank=True)

    class Meta:  # noqa: D106
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):  # noqa: D105
        return f'{self.first_name} {self.last_name} {self.email}'


class AchievementIndividual(models.Model):  # noqa: D101
    name = models.CharField(max_length=45)
    date = models.DateField()
    score = models.DecimalField(max_digits=10, decimal_places=2)
    users_achievement_individual = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)

    class Meta:  # noqa: D106
        verbose_name = 'Achievement Individual'
        verbose_name_plural = 'Achievement Individuals'

    def __str__(self):  # noqa: D105
        return f'{self.name} {self.score}'


class AchievementCompetition(models.Model):  # noqa: D101
    name = models.CharField(max_length=45)
    date = models.DateField()
    score = models.DecimalField(max_digits=10, decimal_places=2)
    user_achievement_competition = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)

    class Meta:  # noqa: D106
        verbose_name = 'Achievement Competition'
        verbose_name_plural = 'Achievement Competitions'

    def __str__(self):  # noqa: D105
        return f'{self.name} {self.score}'


class License(models.Model):  # noqa: D101
    license_is_active = models.BooleanField(default=False)
    date = models.DateField()
    license_type = models.CharField(max_length=150, choices=license_type_consts)
    user_license = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)

    class Meta:  # noqa: D106
        verbose_name = 'Achievement Competition'
        verbose_name_plural = 'Achievement Competitions'

    def __str__(self):  # noqa: D105
        return f'{self.license_is_active} {self.license_type}'
