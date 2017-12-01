from django.conf.urls import url, include
from django.conf import settings

from . import views

from django.contrib.auth.views import logout


urlpatterns = [

    url(r'^$', views.rider, name='index-rider'),

    url(r'^logout/$', logout, {'index': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    url(r'^accounts/', include('registration.backends.simple.urls')),

]