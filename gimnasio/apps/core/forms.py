from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from . import models
from .models import Rutina

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
    def __init__(self, *args, nombre=None, **kwargs):
        super().__init__(*args, **kwargs)
        if nombre:
            self.initial['cliente'] = nombre
            self.fields['cliente'].widget = forms.widgets.TextInput(attrs={'readonly': True})

    class Meta:
        model = Rutina
        fields = ['cliente', 'fecha', 'dia_semana', 'ejercicios']

class DetalleRutinaForm(forms.ModelForm):
    class Meta:
        model = models.DetalleRutina
        fields = "__all__"
    
class ClienteFilterForm(forms.Form):
    cliente = forms.CharField(required=False)

    def filter_clientes(self):
        clientes = Rutina.objects.all()
        print("clientes", clientes)
        if self.is_bound and self.is_valid():
            print("self.is_bound and self.is_valid()", self.is_bound and self.is_valid())
            if self.cleaned_data['cliente']:
                print("self.cleaned_data['cliente']", self.cleaned_data['cliente'])
                clientes = clientes.filter(cliente__nombre__icontains=self.cleaned_data['cliente'])
            print("clientes", clientes)
        return clientes
    