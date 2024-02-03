from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *
app_name = "core"

urlpatterns = [
    path('', index, name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path('gym_admin/', gym_admin, name="gym_admin"),
    path('gym/list/', gym_list, name="gym_list"),
    path('gym/form/', gym_form, name="gym_form"),
    path('gymbro/list/', gymbro_list, name="gymbro_list"),
    path('gymbro/form/', gymbro_form, name="gymbro_form"),
    path('turno/list/', turno_list, name="turno_list"),
    path('turno/form/', turno_form, name="turno_form"),
    path('entrenamiento/list/', entrenamiento_list, name="entrenamiento_list"),
    path('entrenamiento/form/', entrenamiento_form, name="entrenamiento_form"),
    path('ejercicio/list/', ejercicio_list, name="ejercicio_list"),
    path('ejercicio/form/', ejercicio_form, name="ejercicio_form"),
    path('rutina/list/', rutina_list, name="rutina_list"),
    path('rutina/form/', rutina_form, name='rutina_form'),
    path('detallerutina/list/', detallerutina_list, name="detallerutina_list"),
    path('detallerutina/form/', detallerutina_form, name="detallerutina_form"),
    path('consultar-rutinas/', consultar_rutinas, name='consultar_rutinas'),
]
