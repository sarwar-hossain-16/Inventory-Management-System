from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_inv', views.add_inv, name='add_inv'),
    path('add_prod', views.add_prod, name='add_prod'),
    path('check_inv', views.check_inv, name='check_inv'),
    path('home', views.home, name='home'),
    path('rem_prod', views.rem_prod, name='rem_prod'),
    path('rem_inv', views.rem_inv, name='rem_inv'),
]