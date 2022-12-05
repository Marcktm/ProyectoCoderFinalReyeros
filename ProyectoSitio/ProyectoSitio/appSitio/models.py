from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Madre(models.Model):
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 50)
    edad = models.IntegerField()
    peso = models.FloatField()
    datos = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return f"Madre --> {self.nombre}, (EDAD: {self.edad}), (PESO: {self.peso})"

class Bebe(models.Model):

    dia = models.IntegerField()
    mes = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"FPP --> (DÍA: {self.dia}), (MES: {self.mes}), (AÑO: {self.year})"


class Semana(models.Model):

    semana = models.IntegerField()
    datos = models.TextField(max_length=2000, null=True)
    

    def __str__(self):
        return f"Semana {self.semana} de embarazo"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True) 




