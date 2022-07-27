"""Models.py file."""
# Django
from django.db import models

# Project
from accounts.models import Users


class Events(models.Model):  # noqa: D101
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45)
    number_all_participants = models.IntegerField()
    club_member = models.IntegerField()
    outsider = models.IntegerField()

    class Meta:  # noqa: D106
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):  # noqa: D105
        return f'{self.name} {self.number_all_participants}'


class Competition(models.Model):  # noqa: D101
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=5)
    self_weapon_first = models.DecimalField(max_digits=10, decimal_places=2)
    self_weapon_second = models.DecimalField(max_digits=10, decimal_places=2)
    club_weapon_first = models.DecimalField(max_digits=10, decimal_places=2)
    club_weapon_second = models.DecimalField(max_digits=10, decimal_places=2)
    free_space = models.IntegerField()
    events = models.ForeignKey(Events, on_delete=models.CASCADE, null=False)

    class Meta:  # noqa: D106
        verbose_name = 'Competition'
        verbose_name_plural = 'Competitions'

    def __str__(self):  # noqa: D105
        return f'{self.name} {self.code}'


class StarterList(models.Model):  # noqa: D101
    score = models.IntegerField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=False)

    class Meta:  # noqa: D106
        verbose_name = 'Competition'
        verbose_name_plural = 'Competitions'

    def __str__(self):  # noqa: D105
        return f'{self.score} {self.users.first_name} {self.users.last_name}'


class Judge(models.Model):  # noqa: D101
    is_judge = models.BooleanField()
    starter_list = models.ForeignKey(StarterList, on_delete=models.CASCADE)

    class Meta:  # noqa: D106
        verbose_name = 'Judge'
        verbose_name_plural = 'Judges'

    def __str__(self):  # noqa: D105
        return f'{self.is_judge} {self.starter_list}'
