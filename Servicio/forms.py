from django.forms import ModelForm
from .models import Servicio
from django import forms

class FormularioServicio(ModelForm):
    class Meta:
        model = Servicio
        fields = ['imagen','nombre', 'descripcion', 'precio', 'duracion']
        widgets = {
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
            'duracion': forms.TimeInput(attrs={'type': 'time'}),
            'imagen': forms.ClearableFileInput(attrs={'multiple': False}),
        }