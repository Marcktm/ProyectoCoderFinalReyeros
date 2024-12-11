from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from appFinal.models import *
from appFinal.forms import *
from media import *

# Create your views here.

def acercaMi(request):
    return render(request, "appFinal/acerca_mi.html")



@login_required

def experiencias(request):
    exp = Experiencias.objects.all()
    contexto = {"Listado_Exp" : exp}
    
    return render(request, "appFinal/experiencias.html", contexto)

def agregarExperiencia(request):

    if request.method == "POST":
        formulario = ExperienciasForm(request.POST, files = request.FILES)
        print(request.FILES, request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            
            experiencia = Experiencias( name = data["name"], fecha = data["fecha"], datos= data["datos"],image=data["image"])
            experiencia.save()

            return redirect("ap-experiecias")
        
    formulario = ExperienciasForm()
    contexto = {"formulario" : formulario}
    return render(request, "appFinal/agregar_experiencias.html", contexto)

def editarExperiencia(request, id):
    exp = Experiencias.objects.get(id = id)

    if request.method == "POST":
        formulario = ExperienciasForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            exp.name = data["name"]
            exp.fecha = data["fecha"]
            exp.datos = data["datos"]
            exp.image = data["image"]

            exp.save()
            return redirect("ap-experiecias")
        else:
            return render(request, 'appFinal/editar_experiencia.html', {"formulario":formulario, "errores":formulario.errors})

    else:
        formulario = ExperienciasForm(initial={"name" : exp.name, "fecha" : exp.fecha, "datos" : exp.datos, "image" : exp.image})
        return render(request, 'appFinal/editar_experiencia.html', {"formulario":formulario, "errores":""})

def borrarExperiencia(request, id):
    exp = Experiencias.objects.get(id=id)
    exp.delete()
    return redirect("ap-experiecias")




    