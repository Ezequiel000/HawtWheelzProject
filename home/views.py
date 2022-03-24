from django.shortcuts import render
from .models import Car


def homepage(request):
    new_cars = Car.objects.order_by('-date_added')[:5]
    data = {'new_cars': new_cars
            }

    return render(request, 'home/index.html', data)


def inventory(request):
    inventory_cars = Car.objects.all()

    context = {
        'inventory_cars': inventory_cars
    }
    return render(request, 'home/inventory.html',context)