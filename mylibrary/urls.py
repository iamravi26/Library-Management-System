from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
    path('open-resume/', open_resume, name="open-resume"),
]