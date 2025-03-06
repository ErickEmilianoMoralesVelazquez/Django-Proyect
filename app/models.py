from django.db import models
from django.utils.timezone import now

class ErrorLog(models.Model):
    codigo = models.IntegerField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)  # Se usa auto_now_add en lugar de default=now

    class Meta:
        db_table = 'errorlog'
    
    def __str__(self):
        return f"Error {self.codigo} - {self.mensaje}"
