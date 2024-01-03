from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulaire_consommateur, name='Consommateur'),
]
