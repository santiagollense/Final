from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from . import models

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class GymForm(forms.ModelForm):
    class Meta:
        model = models.Gym
        fields = "__all__"

class EstadoForm(forms.ModelForm):
    class Meta:
        model = models.Estado
        fields = "__all__"

class GymbroForm(forms.ModelForm):
    class Meta:
        model = models.Gymbro
        fields = "__all__"

class TurnoForm(forms.ModelForm):
    class Meta:
        model = models.Turno
        fields = "__all__"

class EntrenamientoForm(forms.ModelForm):
    class Meta:
        model = models.Entrenamiento
        fields = "__all__"

class EjercicioForm(forms.ModelForm):
    class Meta:
        model = models.Ejercicio
        fields = "__all__"

class RutinaForm(forms.ModelForm):
    class Meta:
        model = models.Rutina
        fields = "__all__"

class DetalleRutinaForm(forms.ModelForm):
    class Meta:
        model = models.DetalleRutina
        fields = "__all__"