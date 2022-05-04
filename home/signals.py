from django.dispatch import receiver
from .models import Profile
from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def email_confirmed(request, user, **kwargs):
    print('--------user_signed_up')
    prof = Profile.objects.create(owner=user)
    prof.save()

    print('saved the profile for', user.email)
