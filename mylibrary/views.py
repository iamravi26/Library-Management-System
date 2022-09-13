from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):

    return render(request, "mylibrary/dashboard/index.html")

def login(request):
    context = {
        "title":"Login"
    }
    return render(request, "mylibrary/account/login.html", context)

def register(request):
    context = {
        "title":"register"
    }
    return render(request, "mylibrary/account/register.html", context)