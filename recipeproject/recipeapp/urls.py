from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('breakfast/', views.breakfast, name='breakfast'),
    path('lunch/', views.lunch, name='lunch'),
    path('dinner/', views.dinner, name='dinner'),
    path('register/', views.register_view, name='register'),
    path('registration/login/', views.login_view, name='login'),
    path('air-fryer-scones/', views.airFryerScones, name='air-fryer-scones'),
    path('creamy-porridge/', views.creamyPorridge, name='creamy-porridge'),
    path('yoghurt-pancakes/', views.yoghurtPancakes, name='yoghurt-pancakes'),
    path('recipes/create/', views.create_recipe, name='create_recipe'),
    path('recipes/', views.recipe_list, name='recipe_list')
]