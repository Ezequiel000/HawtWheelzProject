from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.http import HttpResponse
from .models import Car


class HomeView(generic.DetailView):
    model = Car
    template_name = 'home/index.html'
