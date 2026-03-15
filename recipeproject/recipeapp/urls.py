from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('breakfast/', views.breakfast, name='breakfast'),
    path('lunch/', views.lunch, name='lunch'),
    path('dinner/', views.dinner, name='dinner'),
    path('register/', views.register_view, name='register'),
    path('registration/login/', views.login_view, name='login'),

    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/create/', views.create_recipe, name='create_recipe'),
    path("recipes/category/<str:category>/", views.recipes_by_category, name="recipes_by_category"),
]