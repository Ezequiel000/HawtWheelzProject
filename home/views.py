from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Profile
from .forms import UserForm, ProfileForm


def homepage(request):
    new_cars = Car.objects.order_by('-date_added')[:5]
    data = {'new_cars': new_cars
            }

    return render(request, 'home/index.html', data)


def inventory(request):
    # this holds all cars in the database
    inventory_cars = Car.objects.all()
    context = {
        'inventory_cars': inventory_cars
    }
    # context contains all data sent
    return render(request, 'home/inventory.html', context)


def about(request):
    return render(request, 'home/about.html')


def login(request):
    return render(request, 'home/login.html')


def car_detail(request, car_id):
    cars = get_object_or_404(Car, id=car_id)

    context = {
        'cars': cars
    }
    return render(request, 'home/detail.html', context)


def user_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
        elif profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your wishlist was successfully updated!')
        else:
            messages.error(request, 'Unable to complete request')
        return redirect('user_profile')

    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    context = {"user": request.user, "user_form": user_form, "profile_form": profile_form}

    return render(request, 'home/wish.html', context)
