from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):

    return HttpResponse("Welcome to My Library")

def login(request):
    context = {
        "title":"Login"
    }
    return render(request, "mylibrary/account/login.html", context)