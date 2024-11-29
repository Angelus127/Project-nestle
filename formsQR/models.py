from django.db import models

class Encuesta(models.Model):
    pregunta = models.CharField(max_length=100)
    producto = models.ForeignKey(
        'analytics.Producto',  
        on_delete=models.CASCADE  
    )


    def __str__(self):
        return self.nombre
