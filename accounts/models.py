# Django
from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):  # noqa: D101
    pesel = models.CharField(max_length=11, blank=True)
    city = models.CharField(max_length=45, blank=True)
    postal_code = models.CharField(max_length=6, blank=True)
    street = models.CharField(max_length=45, blank=True)
    house_number = models.CharField(max_length=45, blank=True)
    phone = models.CharField(blank=True, max_length=15)
    image = models.ImageField(upload_to='Images/', null=True, blank=True)
    club = models.CharField(max_length=20, blank=True)

    class Meta:  # noqa: D106
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):  # noqa: D105

        return f'{self.first_name} {self.last_name} {self.email}'
