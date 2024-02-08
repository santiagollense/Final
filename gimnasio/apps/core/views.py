from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from .forms import CustomAuthenticationForm, CustomUserCreationForm
import calendar
import locale

from django.contrib.auth.models import User

from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

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
        # Crear una instancia de Gymbro con el usuario correspondiente
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
    clientes = Gymbro.objects.all()
    form = RutinaForm(clientes=clientes)
    contexto = {
        "Rutinas": consulta,
        "form": form,
    }
    return render(request, "core/rutina_list.html", contexto)

@login_required
def rutina_form(request):
    nombre = request.GET.get('nombre', None)
    if request.method == "POST":
        form = forms.RutinaForm(request.POST)
        if form.is_valid():
            form.instance.cliente = nombre
            form.save()
            return redirect("core:rutina_list")
    else:
        form = forms.RutinaForm(nombre=nombre)
    return render(request, "core/rutina_form.html", {"form": form, "nombre": nombre})

@login_required
def detallerutina_list(request):

    consulta = DetalleRutina.objects.all()
    contexto = {"DetalleRutinas": consulta}
    return render(request, "core/detallerutina_list.html", contexto)

@login_required
def detallerutina_form(request):
    filtro_form = ClienteFilterForm(request.GET)
    clientes_filtrados = filtro_form.filter_clientes()
    print("clientes_filtrados:", clientes_filtrados)
    if request.method == "POST":
        form = DetalleRutinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:detallerutina_list")
    else:
        form = DetalleRutinaForm()
    
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':  # Verifica si la solicitud es AJAX
        resultados = [{'cliente': cliente.cliente, 'fecha': cliente.fecha, 'dia_semana': cliente.dia_semana} for cliente in clientes_filtrados]
        return JsonResponse(resultados, safe=False)
    else:  # Si no es una solicitud AJAX, devuelve la página HTML
        return render(request, "core/detallerutina_form.html", {"form": form, "filtro_form": filtro_form})
    
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
            rutinas = Rutina.objects.filter(cliente=cliente, fecha__week_day=dia, dia_semana__exact=dia_seleccionado)
        else:
            rutinas = Rutina.objects.filter(cliente=cliente, dia_semana__exact=dia_seleccionado)
    else:
        rutinas = []

    return render(request, 'core/consultar_rutinas.html', {'rutinas': rutinas, 'dias_semana': dias_semana_espanol, 'dia_seleccionado': dia_seleccionado})

