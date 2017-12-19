from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from geoposition.fields import GeopositionField

from rider.models import Travel, RiderProfile


# Create your models here.


class DriverProfile (models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profpic = models.ImageField(upload_to='driver-profpic/', blank=True)

    language = models.CharField(max_length=30, blank=True)

    address = models.CharField(max_length=50, blank=True)

    city = models.CharField(max_length=30, blank=True)

    mobile = models.IntegerField(null=True, blank=True)

    def __str__(self):

        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:

        DriverProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    instance.driverprofile.save()


class Place (models.Model):

    name = models.CharField(max_length=100, blank=True, null=True, default=False)

    position = GeopositionField()


class Vehicle(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    make = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    year = models.DateField(blank=True, null=True, verbose_name="DOB")

    registration = models.CharField(max_length=50)

    image = models.ImageField(upload_to='vehicle-image/', blank=True, default=False)


class Location(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    total_riders = models.IntegerField()

    needed_riders = models.IntegerField()

    place = models.CharField(max_length=100)

    destination = models.CharField(max_length=100)

    position = GeopositionField()


class Reviews(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)

    review = models.TextField(max_length=500)


class Book(models.Model):

    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)

    rider = models.ForeignKey(RiderProfile, on_delete=models.CASCADE)

    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
