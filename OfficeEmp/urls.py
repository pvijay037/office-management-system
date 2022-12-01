from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('AllEmp',views.Allemp, name='Allemp'),
    path('AddEmp',views.Addemp, name='Addemp'),
]