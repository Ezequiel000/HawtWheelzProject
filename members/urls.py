from django.urls import path
from . import views
from .views import register_request

urlpatterns = [

    path('register/', views.register_request, name='register'),


]
