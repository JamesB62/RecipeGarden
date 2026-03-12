from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

# Core Pages
def home(request):
    return render(request, "home.html")

def breakfast(request):
    return render(request, "breakfast.html")

def lunch(request):
    return render(request, "lunch.html")

def dinner(request):
    return render(request, "dinner.html")

# Recipe Pages
def airFryerScones(request):
    return render(request, "recipes/air-fryer-scones.html")

def creamyPorridge(request):
    return render(request, "recipes/creamy-porridge.html")

def yoghurtPancakes(request):
    return render(request, "recipes/yoghurt-pancakes.html")

# User Authentication Forms
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})

def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            error = 'Invalid username or password'

    return render(request, "registration/login.html", {"error": error})