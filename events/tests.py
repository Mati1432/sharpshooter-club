"""Tests.py files."""
# Standard Library
from datetime import datetime
from datetime import timedelta

# Django
from django.test import TestCase
from django.utils import timezone

# Project
from events.models import Events


class EventsModelTest(TestCase):  # noqa D101
    def setUp(self):  # noqa D102
        self.events = Events.objects.create(
            name='Test Name',
            date=datetime.now(tz=timezone.utc).isoformat(' ', 'seconds'),
            city='Test City',
            street='Test Street',
            club_member=4,
            outsider=7,
            number_all_participants=11,
        )

    def test_simple_events_create(self):  # noqa D102
        events = self.events
        self.assertEqual(events.name, 'Test Name')
        self.assertEqual(events.date, datetime.now(tz=timezone.utc).isoformat(' ', 'seconds'))
        self.assertIsNotNone(events)
        self.assertFalse(Events.objects.filter(name='Test Name2').exists())
        self.assertTrue(Events.objects.filter(number_all_participants=11).exists())

    def test_simple_events_update(self):  # noqa D102
        events = self.events
        events.city = 'Test City2'
        events.street = 'Test Street'
        events.save()

        self.assertEqual(events.city, 'Test City2')
        self.assertEqual(events.street, 'Test Street')
        self.assertIsNotNone(events)
        self.assertEqual(events.date, datetime.now(tz=timezone.utc).isoformat(' ', 'seconds'))
        self.assertFalse(Events.objects.filter(city='Test City').exists())

    def test_simple_events_retrieving(self):  # noqa D102
        events_get = Events.objects.get(id=self.events.id)
        self.assertEqual(self.events.id, events_get.id)

    def test_simple_events_delete(self):  # noqa D102
        events_delete = Events.objects.filter(id=self.events.id)
        events_delete.delete()
        self.assertFalse(events_delete.exists())
