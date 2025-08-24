from .views import *
from django.urls import path

urlpatterns = [
    path('bonjour/', bonjour, name='bonjour'),
]