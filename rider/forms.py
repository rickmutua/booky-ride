from django.contrib.auth.models import User
from .models import RiderProfile
from django import forms


class UserForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ('first_name', 'last_name', 'email')


class RiderProfileForm(forms.ModelForm):

    class Meta:

        model = RiderProfile

        fields = ('profpic', 'mobile')