from django import forms
from .models import Recipe

# Recipe Creation Form
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "category",
            "total_time",
            "servings",
            "ingredients",
            "instructions",
            "image",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control", "style": "resize: none;"})
            field.error_messages["required"] = "This field is required."
        self.fields["category"].widget.attrs.update({"class": "form-select"})