import datetime
from django.db import models
from django.utils.html import mark_safe
from django.utils import timezone


class Car(models.Model):
    # Fields
    name = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    date_added = models.DateTimeField('date added', default=timezone.now())
    model = models.CharField(max_length=20)
    # Images require Pillow 9.0
    image = models.ImageField(upload_to='home/images', default='home/images/empty-default.jpg')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def was_added_recently(self):  # will return true if the car was added in the last week
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.date_added <= now


class NavBar(models.Model):
    # Fields
    option_text = models.CharField(max_length=20, default='Text')

    # Methods
    def __str__(self):
        return self.option_text
