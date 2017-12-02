from django.contrib.auth.models import User
from .models import DriverProfile
from django import forms


class UserForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ('first_name', 'last_name', 'email')


class DriverProfileForm(forms.ModelForm):

    class Meta:

        model = DriverProfile

        fields = ('profpic', 'mobile', 'language', 'address', 'city')