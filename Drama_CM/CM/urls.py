from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.main,name=''),
    path('index',views.index,name='index')
]
