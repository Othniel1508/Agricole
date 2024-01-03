from django.urls import path
from . import views

urlpatterns = [
    path('', views.transporteur_view, name='Transporteur'),
]
