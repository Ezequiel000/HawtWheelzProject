from django.db import models


# Create your models here.
# git test

class Car(models.Model):
    # Fields
    name = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    # Images require Pillow 9.0
    product_image = models.ImageField(upload_to='cars')
    price = models.IntegerField()

    # old or used

    # Methods
    def __str__(self):
        return self.name


class NavBar(models.Model):
    # Fields
    option_text = models.CharField(max_length=200)

    # Methods
    def __str__(self):
        return self.option_text
