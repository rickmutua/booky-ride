from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

from django.contrib.auth.views import logout


urlpatterns = [

    url(r'^$', views.rider, name='index-rider'),

    url(r'^update-profile/$', views.update_profile_rider, name='update-profile-rider'),

    url(r'^travel/$', views.travel, name='travel'),

    url(r'^update-travel-details/$', views.update_travel_details, name='update-travel-details'),

    url(r'^driver-list/$', views.driver_list, name='driver-list'),

    url(r'^reviews/(\d+)$', views.rider_review, name='rider-reviews'),

    url(r'^logout/$', logout, {'index': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    url(r'^accounts/', include('registration.backends.simple.urls')),

]


if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)