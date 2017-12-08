from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from geoposition.fields import GeopositionField

# Create your models here.


class RiderProfile (models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profpic = models.ImageField(upload_to='rider-profpic/', blank=True)

    gen_location = models.CharField(max_length=100, blank=True)

    mobile = models.IntegerField(null=True, blank=True)

    def __str__(self):

        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:

        RiderProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    instance.riderprofile.save()


class Place (models.Model):

    name = models.CharField(max_length=100, blank=True, null=True, default=False)

    position = GeopositionField()


class Travel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=100)

    destination = models.CharField(max_length=100)

    position = GeopositionField()


class RiderReview(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rider = models.ForeignKey(RiderProfile, on_delete=models.CASCADE)

    review = models.TextField()


