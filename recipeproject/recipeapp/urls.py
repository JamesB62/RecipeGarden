from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Core
    path('', views.home, name='home'),

    # Accounts
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register_view, name='register'),

    # Password Reset
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name='password_reset_complete'),

    # Recipes
    path('recipes/create/', views.create_recipe, name='create_recipe'),
    path("recipes/category/<str:category>/", views.recipes_by_category, name="recipes_by_category"),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<int:pk>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipes/<int:pk>/delete/', views.delete_recipe, name='delete_recipe'),

    # Search
    path('search/', views.recipe_search, name='recipe_search'),
]