from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserForm, DriverProfileForm
from .models import DriverProfile

from django.db import transaction

from django.core.exceptions import ObjectDoesNotExist

from django.http import Http404

# Create your views here.


@login_required(login_url='/accounts/login')
def driver(request):

    title = 'Drive'

    return render(request, 'base/driver.html', {'title': title})


@login_required(login_url='/accounts/login')
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = DriverProfileForm(request.POST, instance=request.user.driverprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = DriverProfileForm(instance=request.user.driverprofile)
    return render(request, 'profiles/update-profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required(login_url='/accounts/login')
def profile(request, username):

    try:

        user = User.objects.get(username=username)

        profile = DriverProfile.objects.filter(user_id=user).all()

    except ObjectDoesNotExist:

        raise Http404()

    return render(request, 'profiles/profile.html', {'profile': profile})

