from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        min_length=4,
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter username"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter email address"
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter password"
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm password"
        }),
        label="Confirm Password"
    )
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
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
            field.error_messages["required"] = "This field is required"
        self.fields["category"].widget.attrs.update({"class": "form-select"})