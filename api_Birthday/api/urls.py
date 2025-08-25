from .views import *
from django.urls import path

urlpatterns = [
    path('anniversaire/', getAnniversaire, name='getAnniversaire'),
    path('anniversaire/add/', postAnniversaire, name='postAnniversaire'),
    path('anniversaire/today/', Anniversaire_today, name='Anniversaire_today'),
]