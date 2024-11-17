from django.db import models

# Create your models here.
class Servicio(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    duracion = models.DurationField(help_text="Duración en horas y minutos")  # Duración del servicio
    imagen = models.ImageField(upload_to='imagenes/', null=True )  # Imagen del servicio

    def __str__(self):
        return self.nombre