from django.urls import path,include
from appSitio.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("madre/", madre, name="ap-madre"),
    path("madre/crear/", crearMama, name='crear-madre'),
    path("madre/detalle/<pk>/", MadreDetalle.as_view(), name='detalle-madre'),
    path("madre/update/<id>/", editarMadre, name='update-madre'),
    path("madre/delete/<id>/",eliminarMadre, name='delete-madre'),


    path("bebe/", bebe, name='ap-bebe'),
    path("bebe/crear/", creacionBebe, name='crear-bebe'),
    path("bebe/borrar/<id>/", eliminarBebe, name='eliminar-bebe'),

    path("semana/", semana, name='ap-semana'),
    path("semana/crear/", creacionSemana, name='crear-semana'),
    path("semana/buscar/", buscarSemana, name='busc-semana'),
    path('semana/resultado/', resultadoSemana, name='result-semana'),
    path("semana/borrar/<id>/", eliminarSemana, name='eliminar-semana'),
    path("semana/editar/<id>/", editarSemana, name='editar-semana'),
    path("", inicio, name='ap-inicio'),

    path("login/", iniciarSesion, name='ap-login'),
    path("registrar/", registroUsuario, name='ap-registro'),
    path("logout/", LogoutView.as_view(template_name='appSitio/logout.html'), name = "ap-logout"),
    path("perfil/editar/", editarPerfil, name="ap-editarPerfil"),
    path("perfil/avatar/", agregarAvatar, name="ap-avatar"),

     path("", include("appFinal.urls")),

    
]
