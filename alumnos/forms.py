from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'correo', 'matricula', 'edad']

    id = forms.CharField(widget=forms.HiddenInput(), required=False)  # Campo hidden para el ID
