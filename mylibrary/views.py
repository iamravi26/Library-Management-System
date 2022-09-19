from django.shortcuts import render
from django.http import HttpResponse

from mylibrary.models import UserProfile


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


def profile(request):
    # import pdb;pdb.set_trace()
    if request.method == "POST":
        resume = request.FILES.get("resume")
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.resume=resume
        user_profile.save()
    context = {
        "title":"register"
    }
    return render(request, "mylibrary/account/profile.html", context)

def open_resume(request):
    # import pdb;pdb.set_trace()
    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user=request.user)
    context = {
        "title":"register"
    }
    return user_profile.resume.url
