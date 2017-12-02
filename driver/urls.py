from django.conf.urls import url, include
from django.conf import settings

from . import views

from django.contrib.auth.views import logout

from django.views.generic import TemplateView


urlpatterns = [

    url(r'^$', views.driver, name='index-driver'),

    url(r'landing/^$', TemplateView.as_view(template_name='landing.html')),

    url(r'^profile/(?P<username>[-_\w.]+)$', views.profile, name='profile'),

    url(r'^update-profile/$', views.update_profile, name='update-profile'),


    url(r'^logout/$', logout, {'index': settings.LOGOUT_REDIRECT_URL}, name='logout')

]