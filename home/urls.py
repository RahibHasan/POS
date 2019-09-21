from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home',index,name='dashboard'),
    path('custom_login',custom_login,name='custom_login'),
    path('',custom_login,name='front_root')
]
