from django.shortcuts import render, get_object_or_404
from .models import Car
from .filters import CarFilter

def homepage(request):
    new_cars = Car.objects.order_by('-date_added')[:6]
    best_deal = Car.objects.order_by('price')[:6]
    data = {'new_cars': new_cars,
            'best_deal': best_deal
            }

    return render(request, 'home/index.html', data)


def inventory(request):
    #this holds all cars in the database

    car_list = Car.objects.all()
    car_filter = CarFilter(request.GET, queryset=car_list)
    car_list = car_filter.qs

    context = {
        'car_list': car_list, 'car_filter': car_filter
    }
    #context contains all data sent
    return render(request, 'home/inventory.html', context)

def search_results_view(request):
    if request.method == "get":
        car_list = Car.objects.all()
        car_filter = CarFilter(request.GET, queryset=car_list)
        car_list = car_filter.qs
        context = {
            'car_list': car_list, 'car_filter': car_filter
        }
        return render(request, 'home/inventory.html', context)
    else:
        car_list = Car.objects.all()

        return render(request, 'home/inventory.html', {'car_list': car_list})
  

def about(request):
  

    return render(request, 'home/about.html')


def car_detail(request, car_id):
    cars = get_object_or_404(Car, id=car_id)

    context = {
        'cars':cars
    }
    return render(request, 'home/detail.html', context)
