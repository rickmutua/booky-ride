from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from geoposition.fields import GeopositionField


# Create your models here.


class DriverProfile (models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profpic = models.ImageField(upload_to='driver-profpic/', blank=True, default=False)

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