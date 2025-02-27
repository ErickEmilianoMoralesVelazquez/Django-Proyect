# app/models.py
from django.db import models

class ErrorLog(models.Model):
    codigo = models.IntegerField()  # Asegúrate de tener este campo
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=models.functions.Now)  # Usa la fecha actual por defecto

    class Meta:
        db_table = 'errorlog'
    
    def __str__(self):
        return f"Error {self.codigo} - {self.mensaje}"
