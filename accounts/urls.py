"""Urls.py file."""
# Django
from django.urls import include
from django.urls import path

urlpatterns = [
    path('accounts/', include('allauth.urls')),
]
