from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('login/', login, name="login"),
    path('signup/', login, name="signup"),
]