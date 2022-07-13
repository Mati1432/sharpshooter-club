"""Models file."""
# Django
from django.contrib.auth.models import AbstractUser
from django.db import models


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
