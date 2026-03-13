from django.shortcuts import render, redirect
from .forms import RegisterForm, RecipeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Recipe

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

# Recipe Creation Form
@login_required
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect("home")
    else:
        form = RecipeForm()

    return render(request, "recipes/create_recipe.html", {"form": form})

def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})





def recipes_by_category(request, category):

    recipes = Recipe.objects.filter(category=category)

    category_descriptions = {
        "breakfast": "Start your day right with our breakfast recipes. Discover quick, delicious, and wholesome ideas to fuel your morning, from hearty classics to fresh, creative twists.",
        "lunch": "Discover simple, delicious lunch ideas to brighten your day. From quick sandwiches to hearty bowls, our daily recipes make lunchtime easy, healthy, and flavorful.",
        "dinner": "TBC",
        "dessert": "TBC",
        "drink": "TBC",
    }

    description = category_descriptions.get(category, "")

    return render(request, "recipes/category.html", {
        "recipes": recipes,
        "category": category,
        "description": description
    })
