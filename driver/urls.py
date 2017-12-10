from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

from django.contrib.auth.views import logout

from django.views.generic import TemplateView


urlpatterns = [

    url(r'^$', views.driver, name='index-driver'),

    url(r'landing/^$', TemplateView.as_view(template_name='landing.html')),

    url(r'^update-profile/$', views.update_profile_driver, name='update-profile-driver'),

    url(r'^vehicle/$', views.vehicle, name='vehicle'),

    url(r'^update-driver-location-details/$', views.update_driver_location_details, name='update_driver_location_details'),

    url(r'^update-vehicle-details/$', views.update_vehicle_details, name='update-vehicle-details'),

    url(r'^location/$', views.driver_location, name='driver-location'),

    url(r'^review/(\d+)$', views.driver_reviews, name='driver-reviews'),

    url(r'^book/(\d+)$', views.book, name='book'),

    url(r'^logout/$', logout, {'index': settings.LOGOUT_REDIRECT_URL}, name='logout')

]


if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)