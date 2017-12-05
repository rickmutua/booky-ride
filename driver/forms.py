from django.contrib.auth.models import User
from .models import DriverProfile, Vehicle
from django import forms


class UserForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ('first_name', 'last_name', 'email')


class DriverProfileForm(forms.ModelForm):

    class Meta:

        model = DriverProfile

        fields = ('profpic', 'mobile', 'language', 'address', 'city')


class VehicleForm(forms.ModelForm):

    class Meta:

        model = Vehicle

        fields = ('make', 'model', 'year', 'registration', 'image')
