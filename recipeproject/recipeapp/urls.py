from django.urls import path
# from .views import login_view, register_view
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('recipes/create/', views.create_recipe, name='create_recipe'),
    path("recipes/category/<str:category>/", views.recipes_by_category, name="recipes_by_category"),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
]