from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Gym(models.Model):
    nombre = models.CharField(max_length=100)
    dir = models.CharField(max_length=200)
    tel = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    
class Estado(models.Model):
    estado = models.CharField(max_length=100)
    cuota = models.CharField(max_length=100)

    def __str__(self):
        return self.estado
    
class Gymbro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=9)
    fecha_nac = models.DateField(null=True, blank=True)
    inicio_act = models.DateField(default=timezone.now, editable=False, verbose_name="Fecha de inicio de actividad")
    dir = models.CharField(max_length=200)
    tel = models.CharField(max_length=14)
    email = models.EmailField()
    os = models.CharField(max_length=100, verbose_name="Obra Social")

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    turno = models.CharField(max_length=10, default='', blank=True)
    gym = models.ForeignKey(Gym, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.turno

class Entrenamiento(models.Model):
    entrenamiento = models.CharField(max_length=100)
    descripcion = models.TextField(default='Ingrese descripción')

    def __str__(self) -> str:
        return self.entrenamiento

class Ejercicio(models.Model):
    ejercicio = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.ejercicio
    
class DiaSemana(models.Model):
    dia = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.dia

class Rutina(models.Model):
    cliente = models.ForeignKey(Gymbro, on_delete=models.CASCADE)
    fecha = models.DateField()
    dia_semana = models.ForeignKey(DiaSemana, on_delete=models.CASCADE, null=True, blank=True)
    ejercicios = models.ManyToManyField(Ejercicio, through='DetalleRutina')

    def __str__(self) -> str:
        return f"{self.cliente} - {self.fecha} - {self.dia_semana}" 

class DetalleRutina(models.Model):
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    repeticiones = models.IntegerField(blank=True, null=True)
    series = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.rutina} - {self.ejercicio} - Reps: {self.repeticiones} - Series: {self.series}"


