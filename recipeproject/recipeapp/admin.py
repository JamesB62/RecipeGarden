from django.contrib import admin
from .models import Recipe, Subcategory, Holiday

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'total_time', 'servings', 'created_at')
    search_fields = ('title', 'description', 'ingredients')
    list_filter = ('author', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Subcategory)

admin.site.register(Holiday)