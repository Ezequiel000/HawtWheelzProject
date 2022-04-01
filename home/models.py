import datetime
from django.db import models
from django.utils.html import mark_safe
from django.utils import timezone
from django.urls import reverse


class Car(models.Model):
    # Fields
    name = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    date_added = models.DateTimeField('date added')
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20, default='color')
    year = models.IntegerField(default=0)
    # Images require Pillow 9.0
    image = models.ImageField(upload_to='home/images', default='home/images/empty-default.jpg')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500, default= 'des')

    def __str__(self):
        return self.name

    def was_added_recently(self):  # will return true if the car was added in the last week
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.date_added <= now
