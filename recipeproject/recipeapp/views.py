# Django Shortcuts
from django.shortcuts import render, redirect, get_object_or_404

# Django Auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Django Database
from django.db.models import Q

# Local Imports
from .forms import RecipeForm, CustomUserCreationForm
from .models import Recipe, Subcategory

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
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

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
            form.save_m2m()
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
        # "category": category,
        "page_title": f"Daily {category.title()} Recipes",
        "tab_title": category,
        "description": description
    })

# Recipes By Subcategory View
def recipes_by_subcategory(request, subcategory_slug):
    subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
    recipes = Recipe.objects.filter(subcategories=subcategory)
    subcategory_descriptions = {
        "keto": "Discover delicious low-carb recipes designed to fuel your body while keeping carbs in check. From satisfying meals to guilt-free treats, these keto-friendly dishes make it easy to stay on track without sacrificing flavour.",
        "vegetarian": "Explore a vibrant collection of vegetarian recipes packed with fresh ingredients and bold flavours. Whether you're fully plant-based or just looking for meat-free options, these dishes are wholesome, satisfying, and easy to enjoy.",
    }
    description = subcategory_descriptions.get(subcategory.slug, "")
    return render(request, "recipes/category.html", {
        "recipes": recipes,
        "page_title": f"{subcategory.name} Recipes",
        "tab_title": subcategory.name,
        "description": description
    })

# Recipes By Holiday View
def holiday_recipes(request, holiday_slug):
    recipes = Recipe.objects.filter(holidays__slug=holiday_slug)
    page_info = {
        "mothers-day": {
            "title": "Mother's Day Recipes",
            "tab_title": "Mother's Day",
            "description": "Make Mother's Day special with our collection of sweet and savory recipes she'll love. Perfect for breakfast in bed, brunch, or a memorable family meal.",
        },
        "new-years-day": {
            "title": "New Year's Day Recipes",
            "tab_title": "New Year's Day",
            "description": "Celebrate the New Year with recipes that bring joy to the table. From festive breakfasts to indulgent treats and hearty meals, our collection has ideas to make your celebration memorable and delicious.",
        },
    }
    info = page_info.get(holiday_slug, {"title": "Holiday Recipes", "description": ""})
    return render(request, "recipes/category.html", {
        "recipes": recipes,
        "page_title": info["title"],
        "tab_title": info["tab_title"],
        "description": info["description"],
    })

# Recipe Details View
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

# Recipe Edit View
@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.author != request.user:
        return redirect('home')
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})

# Recipe Delete View
@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.author != request.user:
        return redirect('home')
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    return render(request, 'recipes/confirm_delete.html', {'recipe': recipe})

# Recipe Search View
def recipe_search(request):
    query = request.GET.get('q', '') 
    results = []
    if query:
        results = Recipe.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).distinct()
    return render(request, 'search/recipe_search.html', {
        'query': query,
        'results': results
    })