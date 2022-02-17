from django.db import models
from PIL import Image


# Create your models here.

class Car(models.Model):
    # Fields
    name = models.CharField(max_length=200)
           # Images require Pillow 9.0
    product_image = models.ImageField
    price = models.IntegerField


    # Methods
    def __str__(self):
        return self.name


class NavBar(models.Model):
    # Fields
    option_text = models.CharField(max_length=200)

    # Methods
    def __str__(self):
        return self.option_text
