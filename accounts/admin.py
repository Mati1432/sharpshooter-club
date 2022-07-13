"""Admin file."""
# Django
from django.contrib import admin

# Project
# Register your models here.
from accounts.models import Users


@admin.register(Users)
class CustomUserAdmin(admin.ModelAdmin):  # noqa D101
    pass
