from django.db import models

# Create your models here.

class Experiencias(models.Model):

    name = models.CharField(max_length=20)
    fecha = models.DateField()
    datos = models.TextField(max_length=2000, null=True)
    image = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return f"Experiencia de {self.name}, subida el {self.fecha}"

    


