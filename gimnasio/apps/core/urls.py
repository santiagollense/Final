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
    path('gymbro/list/', views.GymBroList.as_view(), name="gymbro_list"),
    path('gymbro/form/', views.gymbro_form, name="gymbro_form"),
    path('gymbro/update/<int:pk>/', views.GymBroUpdate.as_view(), name="gymbro_update"),
    path('gymbro/delete/<int:pk>/', views.GymBroDelete.as_view(), name="gymbro_delete"),
    path('turno/list/', views.turno_list, name="turno_list"),
    path('turno/form/', views.turno_form, name="turno_form"),
    path('entrenamiento/list/', views.entrenamiento_list, name="entrenamiento_list"),
    path('entrenamiento/form/', views.entrenamiento_form, name="entrenamiento_form"),
    path('ejercicio/list/', views.EjercicioList.as_view(), name="ejercicio_list"),
    path('ejercicio/form/', views.EjercicioCreate.as_view(), name="ejercicio_form"),
    path('ejercicio/update/<int:pk>/', views.EjercicioUpdate.as_view(), name="ejercicio_update"),
    path('ejercicio/delete/<int:pk>/', views.EjercicioDelete.as_view(), name="ejercicio_delete"),
    path('rutina/list/', views.RutinaList.as_view(), name="rutina_list"),
    path('rutina/form/', views.rutina_form, name='rutina_form'),
    path('rutina/update/<int:pk>/', views.RutinaUpdate.as_view(), name="rutina_update"),
    path('rutina/delete/<int:pk>/', views.RutinaDelete.as_view(), name="rutina_delete"),
    path('detallerutina/list/', views.DetalleRutinaList.as_view(), name="detallerutina_list"),
    path('detallerutina/form/', views.detallerutina_form, name="detallerutina_form"),
    path('detallerutina/update/<int:pk>/', views.DetalleRutinaUpdate.as_view(), name="detallerutina_update"),
    path('detallerutina/delete/<int:pk>/', views.DetalleRutinaDelete.as_view(), name="detallerutina_delete"),
    path('consultar-rutinas/', views.consultar_rutinas, name='consultar_rutinas'),
]
