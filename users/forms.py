from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'email', 'name', 'surname', 'control_number', 'age', 'tel',
            'password1', 'password2'
        ]

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico',
                'required': True,
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'required': True,
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido',
                'required': True,
            }),
            'control_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de control',
                'required': True,
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad',
                'required': True,
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono',
                'required': True,
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'required': True,
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar contraseña',
                'required': True,
            }),
        }

# class CustomUserLoginForm(AuthenticationForm):
#     pass

import re
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Correo electrónico",
        max_length=150
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("username")  # Django usa "username" en AuthenticationForm
        password = cleaned_data.get("password")

        # Validar que el correo sea del dominio @utez.edu.mx
        if email and not re.match(r"^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$", email):
            raise forms.ValidationError("El correo electrónico debe pertenecer al dominio @utez.edu.mx.")

        # Validar que la contraseña tenga al menos 8 caracteres, un número y un símbolo especial
        if password and not re.match(r"^(?=.*[0-9])(?=.*[!#$%&?]).{8,}$", password):
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres, incluir un número y un símbolo (!, #, $, %, & o ?).")

        # Autenticar usuario
        if email and password:
            user = authenticate(username=email, password=password)
            pass
            if not user:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")

        return cleaned_data
