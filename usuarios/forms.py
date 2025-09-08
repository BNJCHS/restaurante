from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    telefono = forms.CharField(required=False)
    direccion = forms.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "telefono", "direccion", "password1", "password2"]
