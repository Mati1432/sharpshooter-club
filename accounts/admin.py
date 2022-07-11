# Django
from django.contrib import admin

# Register your models here.
from accounts.models import Users


@admin.register(Users)
class CustomUserAdmin(admin.ModelAdmin):  # noqa D101
    pass
