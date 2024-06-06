from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone

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
        model = Gym
        fields = "__all__"

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = "__all__"

class GymbroForm(forms.ModelForm):
    class Meta:
        model = Gymbro
        fields = ['user', 'estado', 'nombre', 'dni', 'fecha_nac', 'dir', 'tel', 'email', 'os']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance.user:
            self.fields['user'].widget.attrs['readonly'] = True  
            self.fields['user'].initial = self.instance.user.username  

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = "__all__"

class EntrenamientoForm(forms.ModelForm):
    class Meta:
        model = Entrenamiento
        fields = "__all__"

class EjercicioForm(forms.ModelForm):
    class Meta:
        model = Ejercicio
        fields = "__all__"

class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = ['cliente', 'fecha', 'dia_semana']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:  
            if self.instance.cliente: 
                self.fields['cliente'].widget.attrs['readonly'] = True 
                self.fields['cliente'].initial = self.instance.cliente
                self.fields['fecha'].initial = timezone.now().date()

class DetalleRutinaForm(forms.ModelForm):
    class Meta:
        model = DetalleRutina
        fields = ['rutina', 'ejercicio', 'repeticiones', 'series']

    def __init__(self, *args, **kwargs):
        cliente_nombre = kwargs.pop('cliente_nombre', None)
        super().__init__(*args, **kwargs)
        if cliente_nombre:
            cliente_instance = Gymbro.objects.filter(nombre=cliente_nombre).first()
            if cliente_instance:
                self.fields['rutina'].queryset = cliente_instance.rutina_set.all()
    
class ClienteFilterForm(forms.Form):
    cliente = forms.CharField(required=False)

    def filter_clientes(self):
        clientes = Rutina.objects.all()
        if self.is_bound and self.is_valid():
            if self.cleaned_data['cliente']:
                clientes = clientes.filter(cliente__nombre__icontains=self.cleaned_data['cliente'])
        return clientes
    