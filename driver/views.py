from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/accounts/login')
def driver(request):

    title = 'Drive'

    return render(request, 'base/driver.html', {'title': title})
