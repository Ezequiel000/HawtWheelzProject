from django.urls import path
from . import views

urlpatterns = [
   path('', views.homepage, name='homepage'),

   path('login/', views.login, name='login'),

   path('inventory/', views.inventory, name='inventory'),

   path('about/', views.about, name='about'),

   path('<int:car_id>', views.car_detail, name="car_detail")
   ]
