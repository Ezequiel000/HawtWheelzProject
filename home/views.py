from django.shortcuts import render
from .models import Car
from .filters import CarFilter

def homepage(request):
    new_cars = Car.objects.order_by('-date_added')[:5]
    data = {'new_cars': new_cars
            }

    return render(request, 'home/index.html', data)

def inventory(request):
    car_list = Car.objects.all()
    car_filter = CarFilter(request.GET, queryset=car_list)
    return render(request, 'home/inventory.html', {'filter': car_filter})