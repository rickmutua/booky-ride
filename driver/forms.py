from django.contrib.auth.models import User
from .models import DriverProfile, Vehicle, Location, Reviews, Book
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


class LocationForm(forms.ModelForm):

    class Meta:

        model = Location

        fields = ('place', 'destination', 'total_riders', 'needed_riders')


class ReviewForm(forms.ModelForm):

    class Meta:

        model = Reviews

        fields = ('review',)


# class BookForm(forms.ModelForm):
#
#     class Meta:
#
#         model = Book
#
#         fields = ('seats',)


