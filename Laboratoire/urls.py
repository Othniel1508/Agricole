from django.urls import path
from . import views

urlpatterns = [
    path('', views.publish_lab, name='Laboratoire'),
]
