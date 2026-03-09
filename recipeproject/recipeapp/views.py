from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def breakfast(request):
    return render(request, "breakfast.html")

def lunch(request):
    return render(request, "lunch.html")

def dinner(request):
    return render(request, "dinner.html")