# Django Forms
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Django Models
from django.contrib.auth.models import User

# Local Imports
from .models import Recipe

# Registration Form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label="Email"
    )
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

# Recipe Creation Form
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "category",
            "subcategories",
            "total_time",
            "servings",
            "ingredients",
            "instructions",
            "image",
        ]
        widgets = {
            "subcategories": forms.CheckboxSelectMultiple
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != "subcategories":
                field.widget.attrs.update({"class": "form-control", "style": "resize: none;"})
                field.error_messages["required"] = "This field is required."
        self.fields["category"].widget.attrs.update({"class": "form-select"})