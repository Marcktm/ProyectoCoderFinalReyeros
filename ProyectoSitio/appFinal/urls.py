from django.urls import path, include
from appFinal.views import *

urlpatterns = [
    path("aboutme/", acercaMi, name="ap-about"),
    path("experiancias/", experiencias, name="ap-experiecias"),
    path("experiancias/crear/", agregarExperiencia, name="ap-crearexperiecias"),
    path("experiancias/editar/<id>/", editarExperiencia, name="ap-editarexperiecias"),
    path("experiancias/borrar/<id>/", borrarExperiencia, name="ap-borrarrexperiecias"),

]
