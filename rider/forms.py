from django.contrib.auth.models import User
from .models import RiderProfile, Place, Travel, RiderReview
from django import forms


class UserForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ('first_name', 'last_name', 'email')


class RiderProfileForm(forms.ModelForm):

    class Meta:

        model = RiderProfile

        fields = ('profpic', 'gen_location', 'mobile')


class PlaceForm(forms.ModelForm):

    class Meta:

        model = Place

        fields = ('name', 'position')


class TravelForm(forms.ModelForm):

    class Meta:

        model = Travel

        fields = ('location', 'destination')


class RiderReviewForm(forms.ModelForm):

    class Meta:

        model = RiderReview

        fields = ('review',)
