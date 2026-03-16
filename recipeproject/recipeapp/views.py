# Django Shortcuts
from django.shortcuts import render, redirect, get_object_or_404

# Django Auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Local Imports
from .forms import RecipeForm
from .models import Recipe

# Core Page Views
def home(request):
    recipe1 = Recipe.objects.get(pk=4)
    recipe2 = Recipe.objects.get(pk=8)
    recipe3 = Recipe.objects.get(pk=12)
    return render(request, "home.html", {
        "recipe1": recipe1,
        "recipe2": recipe2,
        "recipe3": recipe3
    })

# Register View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')

# Recipe Creation View
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

# Recipes By Category View
def recipes_by_category(request, category):
    recipes = Recipe.objects.filter(category=category)
    category_descriptions = {
        "breakfast": "Start your day right with our breakfast recipes. Discover quick, delicious, and wholesome ideas to fuel your morning, from hearty classics to fresh, creative twists.",
        "lunch": "Discover simple, delicious lunch ideas to brighten your day. From quick sandwiches to hearty bowls, our daily recipes make lunchtime easy, healthy, and flavorful.",
        "dinner": "Explore a collection of hearty and flavorful dinner recipes, from quick weeknight meals to indulgent dishes perfect for special occasions. Each recipe is crafted to bring comfort, satisfaction, and a touch of inspiration to your evening table.",
        "dessert": "Indulge your sweet tooth with our collection of irresistible desserts. From quick everyday treats to rich, decadent favourites, there's something here to satisfy every craving and finish your meal on a perfect note.",
        "drinks": "Refresh and recharge with our collection of delicious drinks. From cosy warm beverages to cool, refreshing sips, these recipes are perfect for any time of day.",
    }
    description = category_descriptions.get(category, "")
    return render(request, "recipes/category.html", {
        "recipes": recipes,
        "category": category,
        "description": description
    })

# Recipe Details View
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})