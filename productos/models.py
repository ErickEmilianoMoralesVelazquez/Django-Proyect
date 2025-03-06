from django.db import models


class Detalles_Producto(models.Model):
    descripcion = models.TextField(max_length=400)
    fecha_caducidad = models.DateField()


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

from categorias.models import Categoria

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)


# Campos para relaciones
#  OneToOneField --> 1:1
#  ForeignKey --> 1:M
#  ManyToManyField --> M:M <-- Django crea una tabla intermedia
class Producto(models.Model):
    nombre = models.CharField(max_length=100) # unique=True
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    # 1:1
    detalles_producto = models.OneToOneField(Detalles_Producto, null=True, blank=True, on_delete=models.CASCADE)
    # 1:M
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    # M:M
    proveedor = models.ManyToManyField(Proveedor, blank=True)

    def _str_(self):
        return self.nombre
# Create your models here.


#python manage.py makemigrations productos
#python manage.py migrate