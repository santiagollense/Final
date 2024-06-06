from django.contrib.auth.views import LogoutView
from django.urls import path

#from .views import *
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name="index"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path('gym_admin/', views.gym_admin, name="gym_admin"),
    path('gym/list/', views.GymList.as_view(), name="gym_list"),
    path('gym/form/', views.GymCreate.as_view(), name="gym_form"),
    path('gym/update/<int:pk>/', views.GymUpdate.as_view(), name="gym_update"),
    path('gym/delete/<int:pk>/', views.GymDelete.as_view(), name="gym_delete"),
    path('gymbro/list/', views.gymbro_list, name="gymbro_list"),
    path('gymbro/form/', views.gymbro_form, name="gymbro_form"),
    path('turno/list/', views.turno_list, name="turno_list"),
    path('turno/form/', views.turno_form, name="turno_form"),
    path('entrenamiento/list/', views.entrenamiento_list, name="entrenamiento_list"),
    path('entrenamiento/form/', views.entrenamiento_form, name="entrenamiento_form"),
    path('ejercicio/list/', views.ejercicio_list, name="ejercicio_list"),
    path('ejercicio/form/', views.ejercicio_form, name="ejercicio_form"),
    path('rutina/list/', views.rutina_list, name="rutina_list"),
    path('rutina/form/', views.rutina_form, name='rutina_form'),
    path('detallerutina/list/', views.detallerutina_list, name="detallerutina_list"),
    path('detallerutina/form/', views.detallerutina_form, name="detallerutina_form"),
    path('consultar-rutinas/', views.consultar_rutinas, name='consultar_rutinas'),
]
