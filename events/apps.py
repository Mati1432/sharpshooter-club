"""Apps.py file."""
# Django
from django.apps import AppConfig


class EventsConfig(AppConfig):  # noqa D101
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'
