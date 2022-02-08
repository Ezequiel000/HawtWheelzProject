from django.db import models


# Create your models here.
class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=200)
    year = models.IntegerField
    price = models.IntegerField
    pic = models.ImageField


class User(models.Model):
    id = models.EmailField
