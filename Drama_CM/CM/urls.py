from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.main,name=''),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('create_vote',views.create_vote,name='create_vote')
]
