from django.db import models


class Car(models.Model):
    # Fields
    name = models.CharField(max_length=20, default='Name')
    make = models.CharField(max_length=20, default='Make')

    model = models.CharField(max_length=20, default='Model')
    # Images require Pillow 9.0
    product_image = models.ImageField(upload_to='cars', default='car.jpeg')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class NavBar(models.Model):
    # Fields
    option_text = models.CharField(max_length=20, default='Text')

    # Methods
    def __str__(self):
        return self.option_text
