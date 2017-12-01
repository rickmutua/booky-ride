from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url='/accounts/login')
def rider(request):

    title = 'Ride'

    return render(request, 'base/rider.html', {'title': title})
