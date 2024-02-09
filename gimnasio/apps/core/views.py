from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from .forms import CustomAuthenticationForm, CustomUserCreationForm
import calendar
import locale

from django.contrib import messages
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User

from django.urls import reverse

from django.contrib.auth.decorators import login_required

from . import models
from . import forms

from .models import Rutina, Gymbro, DetalleRutina
from .forms import RutinaForm, ClienteFilterForm, DetalleRutinaForm, GymbroForm


def index(request):
    return render (request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"
    
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            gymbro_instance = form.save()
            username = str(gymbro_instance.username)
            return redirect(reverse("core:gymbro_form") + f"?username={username}")
    else:  # if request.method == "GET":
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})

def gym_admin(request):
    return render (request, "core/gym_admin.html")

@login_required
def gym_list(request):
    consulta = models.Gym.objects.all()
    contexto = {"Gimnasios": consulta}
    return render(request, "core/gym_list.html", contexto)

@login_required
def gym_form(request):
    if request.method == "POST":
        form = forms.GymForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:gym_list")
    else:
        form = forms.GymForm()
    return render (request, "core/gym_form.html", {"form": form})

@login_required
def estado_list(request):
    consulta = models.Estado.objects.all()
    contexto = {"Gimnasios": consulta}
    return render(request, "core/estado_list.html", contexto)

@login_required
def estado_form(request):
    if request.method == "POST":
        form = forms.EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:gym_list")
    else:
        form = forms.GymForm()
    return render (request, "core/gym_form.html", {"form": form})

@login_required
def gymbro_list(request):
    consulta = models.Gymbro.objects.all()
    contexto = {"Gymbros": consulta}
    return render(request, "core/gymbro_list.html", contexto)

@login_required
def gymbro_form(request):
    username = request.GET.get('username')  # Obtener el nombre de usuario de los parámetros de la URL
    user_instance = User.objects.filter(username=username).first()

    if request.method == "POST":
        gymbro_instance = Gymbro(user=user_instance)
        form = GymbroForm(request.POST, instance=gymbro_instance)
        if form.is_valid():
            form.save()
            nombre = gymbro_instance.nombre  # Obtener el nombre del nuevo Gymbro registrado
            return redirect(reverse("core:rutina_form") + f"?nombre={nombre}")
    else:
        if user_instance:
            # Crear una instancia de Gymbro con el usuario correspondiente si está disponible
            gymbro_instance = Gymbro(user=user_instance)
            form = GymbroForm(instance=gymbro_instance)
        else:
            form = GymbroForm()  # Crear un formulario vacío si no se proporciona un nombre de usuario

    return render(request, "core/gymbro_form.html", {"form": form})

@login_required
def turno_list(request):
    consulta = models.Turno.objects.all()
    contexto = {"Turnos": consulta}
    return render(request, "core/turno_list.html", contexto)

@login_required
def turno_form(request):
    if request.method == "POST":
        form = forms.TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:turno_list")
    else:
        form = forms.TurnoForm()
    return render (request, "core/turno_form.html", {"form": form})

@login_required
def entrenamiento_list(request):
    consulta = models.Entrenamiento.objects.all()
    contexto = {"Entrenamientos": consulta}
    return render(request, "core/entrenamiento_list.html", contexto)

@login_required
def entrenamiento_form(request):
    if request.method == "POST":
        form = forms.EntrenamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:entrenamiento_list")
    else:
        form = forms.EntrenamientoForm()
    return render (request, "core/entrenamiento_form.html", {"form": form})

@login_required
def ejercicio_list(request):
    consulta = models.Ejercicio.objects.all()
    contexto = {"Ejercicios": consulta}
    return render(request, "core/ejercicio_list.html", contexto)

@login_required
def ejercicio_form(request):
    if request.method == "POST":
        form = forms.EjercicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:ejercicio_list")
    else:
        form = forms.EjercicioForm()
    return render (request, "core/ejercicio_form.html", {"form": form})

@login_required
def rutina_list(request):
    consulta = Rutina.objects.all()
    contexto = {"Rutinas": consulta}
    return render(request, "core/rutina_list.html", contexto)

@login_required
def rutina_form(request):
    nombre = request.GET.get('nombre') 
    cliente_instance = Gymbro.objects.filter(nombre=nombre).first()

    if request.method == "POST":
        if cliente_instance:
            form = RutinaForm(request.POST)
            if form.is_valid():
                rutina_instance = form.save(commit=False)
                rutina_instance.cliente = cliente_instance
                rutina_instance.save()  
                return redirect(reverse("core:rutina_form") + f"?nombre={nombre}")
        else:
            form = RutinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:rutina_list")
    else:
        if nombre:
            rutina_instance = Rutina(cliente=cliente_instance)
            form = RutinaForm(instance=rutina_instance)
        else:
            form = RutinaForm()

    return render(request, "core/rutina_form.html", {"form": form, "nombre": nombre})


@login_required
def detallerutina_list(request):
    consulta = DetalleRutina.objects.all()
    contexto = {"DetalleRutinas": consulta}
    return render(request, "core/detallerutina_list.html", contexto)

@login_required
def detallerutina_form(request):
    filtro_form = ClienteFilterForm(request.GET)
    cliente_nombre = request.GET.get('nombre') or request.session.get('cliente_nombre')
    if request.method == "GET":
        request.session['cliente_nombre'] = cliente_nombre

    if request.method == "POST":
        print("Entro a POST")
        form = DetalleRutinaForm(request.POST)
        print("form is valid: ", form.is_valid())
        if form.is_valid():
            print("Entro a valid")
            try:
                form.save()
                print("Entro a save")
                messages.success(request, "¡El dato se guardó correctamente!")
                print("Guardado correctamente")
                
                return redirect(reverse("core:detallerutina_form") + f"?nombre={cliente_nombre}")
            except Exception as e:
                messages.error(request, f"Error al guardar el dato: {str(e)}")
        else:
            errors = form.errors.as_data()
            print("Errores de validación del formulario:", errors)
            for field, error_list in errors.items():
                for error in error_list:
                    messages.error(request, f"Error en el campo '{field}': {error}")
            print("Errores de validación del formulario:", form.errors)

    
    form = DetalleRutinaForm(cliente_nombre=cliente_nombre)

    return render(request, "core/detallerutina_form.html", {"form": form, "nombre": cliente_nombre, "filtro_form": filtro_form})

@login_required
def consultar_rutinas(request, dia=None):
    cliente = request.user.gymbro
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    dias_semana = list(calendar.day_name)
    dias_semana_espanol = [dia.capitalize() for dia in dias_semana]
    dia_seleccionado = request.GET.get('dia_semana_espanol')
    if dia_seleccionado:
        dia_seleccionado = dia_seleccionado.capitalize()
        if dia:
            rutinas = Rutina.objects.filter(cliente=cliente, fecha__week_day=dia, dia_semana__dia=dia_seleccionado)
        else:
            rutinas = Rutina.objects.filter(cliente=cliente, dia_semana__dia=dia_seleccionado)
    else:
        rutinas = []

    return render(request, 'core/consultar_rutinas.html', {'rutinas': rutinas, 'dias_semana': dias_semana_espanol, 'dia_seleccionado': dia_seleccionado,'cliente': cliente})

