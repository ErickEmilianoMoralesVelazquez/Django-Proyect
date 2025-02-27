from .models import Producto
from django import forms

class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'imagen']

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input w-100',
                    'placeholder': 'ingrese el nombre del producto'
                }
            )
        }

        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'Ingresa la URL de la foto'
        }

        error_messages = {
            'precio': {
                'required': 'El precio no puede estar vacio',
                'invalid': 'ingresa un valor valido',
                'min_value': 'El precio no puede ser menor a 0'
            }
        }