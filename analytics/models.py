from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)
    imagen_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre