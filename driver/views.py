from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserForm, DriverProfileForm, VehicleForm, LocationForm, ReviewForm
from .models import DriverProfile, Vehicle, Location, Reviews, Book

from rider.models import RiderProfile, Travel

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


@transaction.atomic
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


@transaction.atomic
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


def book(request, id):

    try:
        booked_driver = DriverProfile.objects.get(id=id)
        print(booked_driver)

        rider = RiderProfile.objects.get(id=id)
        print(rider)

        travel = Travel.objects.get(id=id)
        print(travel)

        return render(request, 'book/bookings.html', {'rider': rider, 'travel': travel})

    except ObjectDoesNotExist:

        raise Http404()


# def book(request, id):
#
#     try:
#         booked_driver = DriverProfile.objects.get(id=id)
#         print(booked_driver)
#
#         rider = RiderProfile.objects.get(id=id)
#         print(rider)
#
#         travel = Travel.objects.get(id=id)
#         print(travel)
#
#         booky = Book(driver=booked_driver, rider=rider, travel=travel)
#
#         # print(booky)
#
#         booky.save()
#
#         # if request.method == 'POST':
#         #
#         #     form = BookForm(request.POST)
#         #
#         #     if form.is_valid():
#         #
#         #         booky = form.save(commit=False)
#         #         booky.user = rider
#         #         booky.driver = booked_driver
#         #
#         #         booky.save()
#         #
#         #         return redirect(reverse('book.id'))
#         #
#         #     else:
#         #
#         #         bookings = Book.objects.filter(driver=booked_driver).order_by('-id')
#         #
#         #         form = BookForm()
#         #
#         #         return render(request, 'book/bookings.html', {'bookings': bookings, 'form': form,
#         #                                                       'rider': rider, 'travel': travel})
#         #
#         # else:
#         #
#         #     bookings = Book.objects.filter(driver=booked_driver).order_by('-id')
#         #
#         #     form = BookForm()
#         #
#         #     return render(request, 'book/bookings.html', {'bookings': bookings, 'form': form,
#         #                                                   'rider': rider, 'travel': travel})
#
#     except ObjectDoesNotExist:
#
#         raise Http404()


