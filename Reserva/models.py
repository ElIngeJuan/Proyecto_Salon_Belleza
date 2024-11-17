from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Se crea la clase de la tarea
class Reserva(models.Model):
    servicio = models.CharField(max_length=200)
    fecha_creada = models.DateTimeField(auto_now_add=True) #agrega hora y fecha por defecto
    recomendaciones = models.TextField()
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #relaciona la tarea con el usuario
    
    # Se crea la tarea
    def __str__(self):
        return self.servicio + 'Por: ' + self.usuario.username