import datetime
from django.db import models
from django.utils.html import mark_safe
from django.utils import timezone
from django.urls import reverse

MAKE_CHOICES = {
    ("Tesla", "Tesla"),
    ("Hyundai", "Hyundai"),
    ("Kia", "Kia"),
    ("Polestar", "Polestar"),
    ("FIAT", "FIAT"),
    ("Chevrolet", "Chevrolet"),
    ("Porche", "Porche"),
    ("Audi", "Audi"),
    ("Jeep", "Jeep"),
    ("GMC", "GMC"),
    ("Ford", "Ford")
}

COLOR_CHOICES = {
    ("Black", "Black"),
    ("White", "White"),
    ("Red", "Red"),
    ("Blue", "Blue"),
    ("Green", "Green"),
    ("Silver", "Silver")
}

TYPE_CHOICES = {
    ("SUV", "SUV"),
    ("Compact", "Compact"),
    ("Pick-up", "Pick-up"),
    ("Sedan", "Sedan"),
    ("Sports", "Sports"),
    ("Coupe", "Coupe")
}

class Car(models.Model):
    # Fields
    name = models.CharField(max_length=20)
    make = models.CharField(max_length=20, choices=MAKE_CHOICES, default='make')
    model = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='type', null=True)
    date_added = models.DateTimeField('date added')
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='color')
    year = models.IntegerField(default=0)
    # Images require Pillow 9.0
    image = models.ImageField(upload_to='home/images', default='home/images/empty-default.jpg')
    image1 = models.ImageField(upload_to='home/images', default='home/images/empty-default.jpg')
    image2 = models.ImageField(upload_to='home/images', default='home/images/empty-default.jpg')
    image3 = models.ImageField(upload_to='home/images', default='home/images/empty-default.jpg')
    image4 = models.ImageField(upload_to='home/images', default='home/images/empty-default.jpg')

    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500, default='des')

    def __str__(self):
        return self.name

    def was_added_recently(self):  # will return true if the car was added in the last week
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.date_added <= now

    def get_detail(self):  # will return car info needed for the detail html
        return reverse('car_detail', kwargs={
            'car_id': self.id
        })
