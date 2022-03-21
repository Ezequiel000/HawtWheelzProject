from django.shortcuts import render, get_object_or_404
from .models import Car


def homepage(request):
    new_cars = Car.objects.order_by('-date_added')[:5]
    data = {'new_cars': new_cars
            }

    return render(request, 'home/index.html', data)


def inventory(request):

    return render(request, 'home/inventory.html')