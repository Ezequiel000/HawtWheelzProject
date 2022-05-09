from django.db import models
from home.models import Car
from django.contrib.auth.models import User
from django.db.models.signals import post_save  # add this
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    wishlist = models.ManyToManyField(Car)

    def str(self):
        return f'{self.owner.email} Profile'


