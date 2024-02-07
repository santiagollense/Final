from django.contrib import admin

from . import models

admin.site.register(models.Gym)
admin.site.register(models.Estado)
admin.site.register(models.Gymbro)
admin.site.register(models.Turno)
admin.site.register(models.Entrenamiento)
admin.site.register(models.Ejercicio)
admin.site.register(models.DiaSemana)
admin.site.register(models.Rutina)
admin.site.register(models.DetalleRutina)

