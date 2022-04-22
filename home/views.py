from django.shortcuts import render, get_object_or_404
from .models import Car


def homepage(request):
    new_cars = Car.objects.order_by('-date_added')[:5]
    best_deal = Car.objects.order_by('price')[:6]
    data = {'new_cars': new_cars,
            'best_deal': best_deal,
            }

    return render(request, 'home/index.html', data)


def inventory(request):
    #this holds all cars in the database 

    inventory_cars = Car.objects.all()

    context = {
        'inventory_cars': inventory_cars
    }
    return render(request, 'home/inventory.html', context)#context contains all data sent
  
  

def about(request):
  

    return render(request, 'home/about.html')


def car_detail(request, car_id):
    cars = get_object_or_404(Car, id=car_id)

    context = {
        'cars':cars
    }
    return render(request, 'home/detail.html', context)
