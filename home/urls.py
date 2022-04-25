from django.urls import path
from . import views

urlpatterns = [
   path('', views.homepage, name='homepage'),

   path('inventory/', views.inventory, name='inventory'),

   path('about/', views.about, name='about'),

   path('search_cars/', views.search_cars, name='search_cars')
   ]
