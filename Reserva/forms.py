from django.forms import ModelForm
from .models import Reserva
from django import forms

class FormularioReserva(ModelForm):
    class Meta:
        model = Reserva
        fields = ['servicio', 'recomendaciones', 'fecha_reserva','hora_reserva']
        widgets = {
            'fecha_reserva': forms.DateInput(attrs={'type': 'date'}),
            'hora_reserva': forms.TimeInput(attrs={'type': 'time'}),
        }