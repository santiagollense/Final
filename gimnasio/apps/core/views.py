from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.shortcuts import get_object_or_404
import calendar
import locale

from . import models
from . import forms

def index(request):
    return render (request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"
    
def register(request):
    print("dentro de la funcion register")
    if request.method == "POST":
        print("dentro de POST")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("dentro de is_valid")
            form.save()
            return redirect("core:index")
    else:  # if request.method == "GET":
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})

def gym_admin(request):
    return render (request, "core/gym_admin.html")

def gym_list(request):
    consulta = models.Gym.objects.all()
    contexto = {"Gimnasios": consulta}
    return render(request, "core/gym_list.html", contexto)

def gym_form(request):
    if request.method == "POST":
        form = forms.GymForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:gym_list")
    else:
        form = forms.GymForm()
    return render (request, "core/gym_form.html", {"form": form})

def estado_list(request):
    consulta = models.Estado.objects.all()
    contexto = {"Gimnasios": consulta}
    return render(request, "core/estado_list.html", contexto)

def estado_form(request):
    if request.method == "POST":
        form = forms.EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:gym_list")
    else:
        form = forms.GymForm()
    return render (request, "core/gym_form.html", {"form": form})


def gymbro_list(request):
    consulta = models.Gymbro.objects.all()
    contexto = {"Gymbros": consulta}
    return render(request, "core/gymbro_list.html", contexto)

def gymbro_form(request):
    if request.method == "POST":
        form = forms.GymbroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:gymbro_list")
    else:
        form = forms.GymbroForm()
    return render (request, "core/gymbro_form.html", {"form": form})

def turno_list(request):
    consulta = models.Turno.objects.all()
    contexto = {"Turnos": consulta}
    return render(request, "core/turno_list.html", contexto)

def turno_form(request):
    if request.method == "POST":
        form = forms.TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:turno_list")
    else:
        form = forms.TurnoForm()
    return render (request, "core/turno_form.html", {"form": form})

def entrenamiento_list(request):
    consulta = models.Entrenamiento.objects.all()
    contexto = {"Entrenamientos": consulta}
    return render(request, "core/entrenamiento_list.html", contexto)

def entrenamiento_form(request):
    if request.method == "POST":
        form = forms.EntrenamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:entrenamiento_list")
    else:
        form = forms.EntrenamientoForm()
    return render (request, "core/entrenamiento_form.html", {"form": form})

def ejercicio_list(request):
    consulta = models.Ejercicio.objects.all()
    contexto = {"Ejercicios": consulta}
    return render(request, "core/ejercicio_list.html", contexto)

def ejercicio_form(request):
    if request.method == "POST":
        form = forms.EjercicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:ejercicio_list")
    else:
        form = forms.EjercicioForm()
    return render (request, "core/ejercicio_form.html", {"form": form})

def rutina_list(request):
    consulta = models.Rutina.objects.all()
    contexto = {"Rutinas": consulta}
    return render(request, "core/rutina_list.html", contexto)

def rutina_form(request, cliente_id):
    cliente = get_object_or_404(models.Gymbro, pk=cliente_id)
    if request.method == "POST":
        form = forms.RutinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:rutina_list")
    else:
        form = forms.RutinaForm(initial={'cliente': cliente})
    return render (request, "core/rutina_form.html", {"form": form})

def detallerutina_list(request):
    consulta = models.DetalleRutina.objects.all()
    contexto = {"DetalleRutinas": consulta}
    return render(request, "core/detallerutina_list.html", contexto)

def detallerutina_form(request):
    if request.method == "POST":
        form = forms.DetalleRutinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:detallerutina_list")
    else:
        form = forms.DetalleRutinaForm()
    return render (request, "core/detallerutina_form.html", {"form": form})

from django.contrib.auth.decorators import login_required

@login_required
def consultar_rutinas(request):
    usuario = request.user
    rutinas = models.Rutina.objects.filter(cliente__user=usuario)
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    dias_semana = list(calendar.day_name)
    dias_semana_espanol = [dia.capitalize() for dia in dias_semana]
    dia_seleccionado = request.GET.get('dia_semana_espanol')
    
    print(f"Día seleccionado: {dia_seleccionado}")

    if dia_seleccionado:
        rutinas = rutinas.filter(dia_semana__icontains=dia_seleccionado)

    return render(request, 'core/consultar_rutinas.html', {'rutinas': rutinas, 'dias_semana': dias_semana_espanol, 'dia_seleccionado': dia_seleccionado})
