from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserForm, DriverProfileForm, VehicleForm, LocationForm, ReviewForm
from .models import DriverProfile, Vehicle, Location, Reviews

from django.db import transaction

from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from django.http import Http404, JsonResponse

# Create your views here.


@login_required(login_url='/accounts/login')
def driver(request):

    current_user = request.user

    try:

        profile = DriverProfile.objects.get(user=current_user)

    except ObjectDoesNotExist:

        raise Http404()

    title = 'Drive'

    return render(request, 'base/driver.html', {'title': title, 'profile': profile})


@login_required(login_url='/accounts/login')
@transaction.atomic
def update_profile_driver(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = DriverProfileForm(request.POST, instance=request.user.driverprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('index-driver')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = DriverProfileForm(instance=request.user.driverprofile)
    return render(request, 'base/update-profile-driver.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def vehicle(request):

    current_user = request.user

    try:

        car = Vehicle.objects.filter(user=current_user).all()

    except ObjectDoesNotExist:

        raise Http404()

    title = 'vehicle'

    return render(request, 'vehicles/vehicle.html', {'car': car, 'title': title})


def update_vehicle_details(request):

    current_user = request.user

    try:

        if request.method == 'POST':

            form = VehicleForm(request.POST, files=request.FILES)

            if form.is_valid():

                single_vehicle = form.save(commit=False)

                single_vehicle.user = current_user

                single_vehicle.save()

                return redirect(reverse('vehicle'))

            else:

                form = VehicleForm()

                return render(request, 'vehicles/update-vehicle-details.html', {'form': form})

        else:

            form = VehicleForm()

            return render(request, 'vehicles/update-vehicle-details.html', {'form': form})

    except ObjectDoesNotExist:

        raise Http404()


def driver_location(request):

    current_user = request.user

    try:

        car = Vehicle.objects.filter(user=current_user).all()

        location = Location.objects.filter(user=current_user).all()

    except ObjectDoesNotExist:

        raise Http404()

    return render(request, 'locations/location.html', {'location': location, 'car': car})


def update_driver_location_details(request):

    current_user = request.user

    try:

        if request.method == 'POST':

            form = LocationForm(request.POST)

            if form.is_valid():

                update = form.save(commit=False)

                update.user = current_user

                update.save()

                return redirect(reverse('driver-location'))

            else:

                form = LocationForm()

                return render(request, 'locations/update-driver-location.html', {'form': form})

        else:

            form = LocationForm()

            return render(request, 'locations/update-driver-location.html', {'form': form})

    except ObjectDoesNotExist:

        raise Http404()


def driver_reviews(request, id):

    driver_review = DriverProfile.objects.get(id=id)

    comments = Reviews.objects.filter(driver=driver_review.id).order_by('-id')

    try:

        if request.method == 'POST':

            form = ReviewForm(request.POST)

            if form.is_valid():

                comment = form.save(commit=False)
                comment.user = request.user
                comment.driver = driver_review

                comment.save()

                return redirect(reverse('driver-reviews'))

            else:

                comments = Reviews.objects.filter(driver=driver_review).order_by('-id')

                form = ReviewForm()

                return render(request, 'base/reviews.html', {'form': form, 'comments': comments})

        else:

            comments = Reviews.objects.filter(driver=driver_review).order_by('-id')

            form = ReviewForm()

            return render(request, 'base/reviews.html', {'form': form, 'comments': comments})

    except ObjectDoesNotExist:

        raise Http404()

#
# def review(request):
#
#     current_user = request.user
#
#     review = request.POST.get('review')
#
#     comment = Reviews(review = review)
#
#     comment.user = current_user
#
#     comment.save()
#
#     data = {'Success': 'Reviewed'}
#
#     return JsonResponse(data)







# @login_required(login_url='/accounts/login')
# def driver_profile(request, username):
#
#     try:
#
#         user = User.objects.get(username=username)
#
#         profile = DriverProfile.objects.filter(user_id=user).all()
#
#     except ObjectDoesNotExist:
#
#         raise Http404()
#
#     return render(request, 'profiles/profile.html', {'profile': profile})

