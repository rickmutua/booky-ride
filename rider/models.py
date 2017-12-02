from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class RiderProfile (models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profpic = models.ImageField(upload_to='rider-profpic/', blank=True, default=False)

    mobile = models.IntegerField(null=True, blank=True)

    def __str__(self):

        return self.user.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:

        RiderProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    instance.riderprofile.save()