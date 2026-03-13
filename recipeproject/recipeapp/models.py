from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):

    CATEGORY_CHOICES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
        ("dessert", "Dessert"),
        ("drink", "Drink"),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    total_time = models.PositiveIntegerField(help_text="Time in minutes")
    servings = models.PositiveIntegerField()

    ingredients = models.TextField(help_text="List ingredients separated by lines")
    instructions = models.TextField(help_text="Write the step-by-step instructions")

    image = models.ImageField(upload_to="recipes/", blank=True, null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title