from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Subcategory Model
class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Holiday Model
class Holiday(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

# Recipe Creation Model
class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
        ("dessert", "Dessert"),
        ("drinks", "Drinks"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    subcategories = models.ManyToManyField(Subcategory, blank=True)
    holidays = models.ManyToManyField(Holiday, blank=True)
    total_time = models.PositiveIntegerField(help_text="Time in minutes")
    servings = models.PositiveIntegerField()
    ingredients = models.TextField(help_text="List ingredients separated by lines")
    instructions = models.TextField(help_text="Write the step-by-step instructions")
    image = models.ImageField(upload_to="recipes/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title