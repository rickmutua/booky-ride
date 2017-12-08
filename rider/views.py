from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserForm, RiderProfileForm, TravelForm, RiderReviewForm
from .models import RiderProfile, Travel, RiderReview

from django.db import transaction

from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from django.http import Http404


# Create your views here.


@login_required(login_url='/accounts/login')
def rider(request):

    current_user = request.user

    try:

        profile = RiderProfile.objects.get(user=current_user)

    except ObjectDoesNotExist:

        raise Http404()

    title = 'Ride'

    return render(request, 'base/rider.html', {'title': title, 'profile': profile})


@login_required(login_url='/accounts/login')
@transaction.atomic
def update_profile_rider(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = RiderProfileForm(request.POST, instance=request.user.riderprofile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('index-rider')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = RiderProfileForm(instance=request.user.riderprofile)
    return render(request, 'base/update-profile-rider.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def travel(request):

    current_user = request.user

    try:

        profile = RiderProfile.objects.filter(user=current_user).all()

        traveling = Travel.objects.filter(user=current_user).all()

    except ObjectDoesNotExist:

        raise Http404()

    return render(request, 'travels/travel.html', {'profile': profile, 'traveling': traveling})


def update_travel_details(request):

    current_user = request.user

    try:

        if request.method == 'POST':

            form = TravelForm(request.POST)

            if form.is_valid():

                single_travel = form.save(commit=False)

                single_travel.user = current_user

                single_travel.save()

                return redirect(reverse('travel'))

            else:

                form = TravelForm()

                return render(request, 'travels/update-travel-details', {'form': form})

        else:

            form = TravelForm()

            return render(request, 'travels/update-travel-details.html', {'form': form})

    except ObjectDoesNotExist:

        raise Http404()


def driver_list(request):

    return render(request, 'base/driver-list.html')


def rider_review(request, id):

    review_rider = RiderProfile.objects.get(id=id)

    try:

        if request.method == 'POST':

            form = RiderReviewForm(request.POST)

            if form.is_valid():

                comment = form.save(commit=False)
                comment.user = request.user
                comment.rider = review_rider

                comment.save()

                return redirect(reverse('rider-reviews'))

            else:

                comments = RiderReview.objects.filter(rider=review_rider).order_by('-id')

                form = RiderReviewForm()

                return render(request, 'base/rider-reviews.html', {'form': form, 'comments': comments})

        else:

            comments = RiderReview.objects.filter(rider=review_rider).order_by('-id')

            form = RiderReviewForm()

            return render(request, 'base/rider-reviews.html', {'form': form, 'comments': comments})

    except ObjectDoesNotExist:

        raise Http404()






# @login_required(login_url='/accounts/login')
# def rider_profile(request, username):
#
#     try:
#
#         user = User.objects.get(username=username)
#
#         profile = RiderProfile.objects.filter(user_id=user).all()
#
#     except ObjectDoesNotExist:
#
#         raise Http404()
#
#     return render(request, 'profiles/profile.html', {'profile': profile})


# def place(request, username):
#
#     user = User.objects.get(username=username)
#
#     try:
#
#         if request.method == 'POST':
#
#             place_form = PlaceForm(request.Post)
#
#             if place_form.is_valid():
#
#                 city = place_form.save(commit=False)
#                 city.user = user
#                 city.save()
#
#                 return redirect(reverse('rider'))
#         else:
#
#             place_form = PlaceForm()
#
#             return render(request, 'base/rider.html', {'place_form': place_form})
#
#     except ObjectDoesNotExist:
#
#         raise Http404()




