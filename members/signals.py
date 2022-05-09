# Signals.py

from .models import Profile
from allauth.account.signals import user_signed_up
from django.dispatch import receiver  # add this
from django.db.models.signals import post_save  # add this
from django.contrib.auth.models import User


@receiver(user_signed_up)
def email_confirmed(request, user, **kwargs):
    print('--------user_signed_up')
    prof = Profile.objects.create(owner=user)
    prof.save()

    print('saved the profile for', user.email)


@receiver(post_save, sender=User)  # add this
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)
        print('created the profile')


@receiver(post_save, sender=User)  # add this
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    print('saved the profile')
