from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, RecipeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Recipe

# Core Pages
def home(request):
    recipe1 = Recipe.objects.get(pk=4)
    recipe2 = Recipe.objects.get(pk=8)
    recipe3 = Recipe.objects.get(pk=12)

    return render(request, "home.html", {
        "recipe1": recipe1,
        "recipe2": recipe2,
        "recipe3": recipe3
    })

def breakfast(request):
    return render(request, "breakfast.html")

def lunch(request):
    return render(request, "lunch.html")

def dinner(request):
    return render(request, "dinner.html")

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

# View Recipes By Category
def recipes_by_category(request, category):

    recipes = Recipe.objects.filter(category=category)

    category_descriptions = {
        "breakfast": "Start your day right with our breakfast recipes. Discover quick, delicious, and wholesome ideas to fuel your morning, from hearty classics to fresh, creative twists.",
        "lunch": "Discover simple, delicious lunch ideas to brighten your day. From quick sandwiches to hearty bowls, our daily recipes make lunchtime easy, healthy, and flavorful.",
        "dinner": "Explore a collection of hearty and flavorful dinner recipes, from quick weeknight meals to indulgent dishes perfect for special occasions. Each recipe is crafted to bring comfort, satisfaction, and a touch of inspiration to your evening table.",
        "dessert": "TBC",
        "drink": "TBC",
    }

    description = category_descriptions.get(category, "")

    return render(request, "recipes/category.html", {
        "recipes": recipes,
        "category": category,
        "description": description
    })

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})