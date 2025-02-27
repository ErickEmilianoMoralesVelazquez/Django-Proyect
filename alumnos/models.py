from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    # matricula unica
    matricula = models.CharField(max_length=10, unique=True)
    # correo unico
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
    
#     {
#         "id": 1,
#         "nombre": "Erick Emiliano",
#         "apellido": "Morales Velazquez",
#         "edad": 20,
#         "matricula": "20223tn101",
#         "correo": "20223tn101@utez.edu.mx"
# }
    
