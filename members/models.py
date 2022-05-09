from django.db import models
from home.models import Car
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    wishlist = models.ManyToManyField(Car)

    def str(self):
        return f'{self.owner.email} Profile'
