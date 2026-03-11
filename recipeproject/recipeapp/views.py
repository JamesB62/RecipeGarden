from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import login

# Create your views here.

def home(request):
    return render(request, "home.html")

def breakfast(request):
    return render(request, "breakfast.html")

def lunch(request):
    return render(request, "lunch.html")

def dinner(request):
    return render(request, "dinner.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})