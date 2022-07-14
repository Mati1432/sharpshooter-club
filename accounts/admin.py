"""Admin file."""
# Django
from django.contrib import admin

# Project
from accounts.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):  # noqa D101
    list_display = [
        'first_name',
        'last_name',
        'pesel',
        'city',
        'postal_code',
        'street',
        'house_number',
    ]
    list_filter = [
        'last_name',
    ]
    list_display_links = (
        'last_name',
    )
    list_editable = [
        'pesel',
        'city',
        'postal_code',
        'street',
        'house_number',
    ]
