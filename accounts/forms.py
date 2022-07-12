"""Forms files."""
# Standard Library
import datetime

# Django
from django import forms

# 3rd-party
from allauth.account.forms import SignupForm

# Project
from accounts.models import Users


class SignUpForm(SignupForm):  # noqa D101
    first_name = forms.CharField(
        label='First name',
        max_length=254
    )
    last_name = forms.CharField(
        label='Last name',
        max_length=254
    )
    city = forms.CharField(
        label='city',
        max_length=254
    )
    pesel = forms.CharField(
        label='pesel',
        max_length=11
    )
    postal_code = forms.CharField(
        label='postal_code',
        max_length=7
    )
    street = forms.CharField(
        label='street',
        max_length=254
    )
    house_number = forms.CharField(
        label='house_number',
        max_length=254
    )
    phone = forms.CharField(
        label='phone',
        max_length=15
    )
    image = forms.ImageField(
        required=False,
    )
    club = forms.CharField(
        label='club',
        max_length=20,
    )
    date_brith = forms.DateField(
        initial=datetime.date.today,
        widget=forms.widgets.DateInput(
            attrs={'type': 'date'},
        ),
    )
    class Meta:  # noqa D106
        model = Users
        fields = [
            'first_name',
            'last_name',
            'city',
            'date',
        ]

    def save(self, request):  # noqa D102
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        city = self.cleaned_data['city']
        pesel = self.cleaned_data['pesel']
        postal_code = self.cleaned_data['postal_code']
        street = self.cleaned_data['street']
        house_number = self.cleaned_data['house_number']
        phone = self.cleaned_data['phone']
        image = self.cleaned_data['image']
        club = self.cleaned_data['club']
        date_brith = self.cleaned_data['date_brith']

        user = super().save(request)

        user.first_name = first_name
        user.last_name = last_name
        user.city = city
        user.pesel = pesel
        user.postal_code = postal_code
        user.street = street
        user.house_number = house_number
        user.phone = phone
        user.image = image
        user.club = club
        user.birth_date = date_brith

        user.save()
        return user
