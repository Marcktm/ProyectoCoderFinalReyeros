from django.shortcuts import render, redirect
from django.http import HttpResponse
from appSitio.models import *
from appSitio.forms import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

def inicio(request):
    try:
        if request.user.is_authenticated:
            imagen_model= Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
            imagen_url = imagen_model.imagen.url
        
        else:
            imagen_url = ""
        return render(request, "appSitio/index.html", {"imagen_url": imagen_url})
    except:
        return redirect('ap-avatar')

@login_required
def madre(request):
    madre = Madre.objects.filter(user= request.user.id)
    contexto = {"MADRE": madre}
    return render(request, "appSitio/madre.html", contexto)

@login_required
def bebe(request):
    bebe = Bebe.objects.all()
    contexto = {"FECHA" : bebe}
    return render(request, "appSitio/bebe.html", contexto)

@login_required
def semana(request):
    semana = Semana.objects.all()
    contexto = {"Listado_Semanas" : semana}
    return render(request, "appSitio/semana.html", contexto)

def creacionBebe(request):
    if request.method == "POST":
        formulario = BebeFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            dia2 = int
            mes = int
            year = int

            if data["year"] % 4 == 0 and not data["year"] % 100 == 0 or data["year"] % 400 == 0:
                if data["mes"] == 1 or data["mes"] == 3 or data["mes"] == 5 or data["mes"] == 7 or data["mes"] == 8:
                    data["dia"] = data["dia"] + 7
                    if data["dia"] > 31:
                        data["dia"] = data["dia"] - 31 
                    data["mes"] = data ["mes"] - 3
                    if data["mes"] <= 0:
                        if data["mes"] == 0:
                            data["mes"] = 12
                        elif data["mes"] == -1 :
                            data["mes"] = 11
                        else :
                            data["mes"] = 10
                    else:
                        data["year"] = data["year"]+1
                        
                    bebe = Bebe(dia = data["dia"], mes = data["mes"], year = data["year"])
                    bebe.save()
                elif data["mes"] == 4 or data["mes"] == 6 or data["mes"] == 9 or data["mes"] == 11:
                    data["dia"] = data["dia"] + 7
                    if data["dia"] > 30:
                        data["dia"] = data["dia"] - 30 
                    data["mes"] = data ["mes"] - 3
                    if data["mes"] <= 0:
                        if data["mes"] == 0:
                            data["mes"] = 12
                        elif data["mes"] == -1 :
                            data["mes"] = 11
                        else :
                            data["mes"] = 10
                    else:
                        data["year"] = data["year"]+1
                    bebe = Bebe(dia = data["dia"], mes = data["mes"], year = data["year"])
                    bebe.save()
                else:
                    data["dia"] = data["dia"] + 7
                    if data["dia"] > 28:
                        data["dia"] = data["dia"] - 28 
                    data["mes"] = data ["mes"] - 3
                    if data["mes"] <= 0:
                        if data["mes"] == 0:
                            data["mes"] = 12
                        elif data["mes"] == -1 :
                            data["mes"] = 11
                        else :
                            data["mes"] = 10
                    else:
                        data["year"] = data["year"]+1
                    bebe = Bebe(dia = data["dia"], mes = data["mes"], year = data["year"])
                    bebe.save()
            
            else:
                if data["mes"] == 1 or data["mes"] == 3 or data["mes"] == 5 or data["mes"] == 7 or data["mes"] == 8:
                    data["dia"] = data["dia"] + 7
                    if data["dia"] > 31:
                        data["dia"] = data["dia"] - 31 
                    data["mes"] = data ["mes"] - 3
                    if data["mes"] <= 0:
                        if data["mes"] == 0:
                            data["mes"] = 12
                        elif data["mes"] == -1 :
                            data["mes"] = 11
                        else :
                            data["mes"] = 10
                    else:
                        data["year"] = data["year"]+1
                        
                    bebe = Bebe(dia = data["dia"], mes = data["mes"], year = data["year"])
                    bebe.save()
                elif data["mes"] == 4 or data["mes"] == 6 or data["mes"] == 9 or data["mes"] == 11:
                    data["dia"] = data["dia"] + 7
                    if data["dia"] > 30:
                        data["dia"] = data["dia"] - 30 
                    data["mes"] = data ["mes"] - 3
                    if data["mes"] <= 0:
                        if data["mes"] == 0:
                            data["mes"] = 12
                        elif data["mes"] == -1 :
                            data["mes"] = 11
                        else :
                            data["mes"] = 10
                    else:
                        data["year"] = data["year"]+1
                    bebe = Bebe(dia = data["dia"], mes = data["mes"], year = data["year"])
                    bebe.save()
                else:
                    data["dia"] = data["dia"] + 7
                    if data["dia"] > 28:
                        data["dia"] = data["dia"] - 28 
                    data["mes"] = data ["mes"] - 3
                    if data["mes"] <= 0:
                        if data["mes"] == 0:
                            data["mes"] = 12
                        elif data["mes"] == -1 :
                            data["mes"] = 11
                        else :
                            data["mes"] = 10
                    else:
                        data["year"] = data["year"]+1
                    bebe = Bebe(dia = data["dia"], mes = data["mes"], year = data["year"])
                    bebe.save()


            return redirect('ap-bebe')
    
    formulario = BebeFormulario() 

    contexto = {"formulario" : formulario}
    return render(request, "appSitio/bebe_formulario.html", contexto)

def eliminarBebe(request, id):
    bebe = Bebe.objects.get(id=id)
    bebe.delete()
    return redirect('ap-bebe')


def creacionSemana(request):
    if request.method == "POST":
        formulario = SemanaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            semana = Semana(semana = data["semana"], datos = data["datos"])
            semana.save()

            return redirect('ap-semana')
    
    formulario = SemanaFormulario()

    contexto = {"formulario" : formulario}
    return render(request, "appSitio/semana_formulario.html", contexto)

def buscarSemana(request):
    return render(request, "appSitio/buscar_semana.html")

def resultadoSemana(request):
    res_semana = request.GET["nro_semana"]
    semanas = Semana.objects.filter(semana__icontains = res_semana)
    return render(request, "appSitio/resultado_semana.html", {"Semanas" : semanas})

def eliminarSemana(request, id):
    semana = Semana.objects.get(id=id)
    semana.delete()
    return redirect('ap-semana')

def editarSemana(request, id):
    semana = Semana.objects.get(id = id)

    if request.method == "POST":
        formulario = SemanaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            semana.semana = data["semana"]
            semana.datos = data["datos"]
            semana.save()
            return redirect('ap-semana')
        else:
            return render(request, 'appSitio/editar_semana.html', {"formulario":formulario, "errores":formulario.errors})

    else:
        formulario = SemanaFormulario(initial={"semana" : semana.semana, "datos" : semana.datos})
        return render(request, 'appSitio/editar_semana.html', {"formulario":formulario, "errores":""})

    
    
#class MadreList(LoginRequiredMixin, ListView):
 #   model = Madre
  #  template_name = "appSitio/madre.html"

class MadreDetalle(DetailView):
    model = Madre
    template_name = "appSitio/madre_detalle.html"

@login_required
def crearMama(request):
    if request.method == "POST":
        formulario = MadreFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = request.user
            madre = Madre(user = usuario, nombre = data["nombre"], edad = data["edad"], peso = data["peso"], datos = data["datos"])
            madre.save()

            return redirect("ap-madre")
        
        else:
            return render(request, "appSitio/madre_formulario.html", {"form": formulario, "errors": formulario.errors})
    formulario = MadreFormulario()
    return render(request, "appSitio/madre_formulario.html", {"form": formulario})




def editarMadre(request, id):
    madre = Madre.objects.get(id = id)
    if request.method == "POST":
        formulario = MadreFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            madre.nombre = data["nombre"]
            madre.edad = data["edad"]
            madre.peso = data["peso"]
            madre.datos = data["datos"]
            madre.save()
            return redirect('ap-madre')
        else:
            return render(request, 'appSitio/madre_form.html', {"formulario":formulario, "errores":formulario.errors})

    else:
        formulario = MadreFormulario(initial={"nombre" : madre.nombre, "edad" : madre.edad, "peso" : madre.peso, "datos":madre.datos })
        return render(request, 'appSitio/madre_form.html', {"formulario":formulario, "errores":""})
    
    
def eliminarMadre(request, id):
    madre = Madre.objects.get(id=id)
    madre.delete()
    return redirect('ap-madre')

def iniciarSesion(request):
    errors = ""
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user= authenticate(username = data["username"], password = data["password"])

            if user is not None:
                    login(request, user)
                    return redirect('ap-inicio')
            else:
                return render(request, 'appSitio/login.html', {"form": formulario, "errors": "Credenciale Invalidas"})
        else:
           return render(request, 'appSitio/login.html', {"form": formulario, "errors": formulario.errors})    
    
    formulario = AuthenticationForm()
    return render(request, "appSitio/login.html", {"form": formulario, "errors": errors})
    
def registroUsuario(request):

    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            return redirect("ap-inicio")
        

        else: 
            return render(request, "appSitio/registro.html", {"form": formulario, "errors": formulario.errors})

    formulario = UserRegisterForm()

    return render(request, "appSitio/registro.html", {"form": formulario})

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        #CARGAR INFO EN EL FORM
        formulario = UserEditForm(request.POST)
        #VALIDACION DEL FORM
        if formulario.is_valid():
            data = formulario.cleaned_data
        #ACTUALIZACION DEL FORM

            usuario.email = data["email"]
            usuario.last_name = data["last_name"]

            usuario.save()

            return redirect("ap-inicio")
        else:
            return render(request, "appSitio/editar_perfil.html", {"form": formulario, "errors": formulario.errors})
    else:
        #FORM PRINCIPAL
        formulario = UserEditForm(initial = {"email": usuario.email, "last_name" : usuario.last_name})
        

    return render(request, "appSitio/editar_perfil.html", {"form": formulario})


@login_required
def agregarAvatar(request):

    if request.method == "POST":
        formulario = AvatarForm(request.POST, files = request.FILES)
        print(request.FILES, request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            usuario = request.user

            avatar = Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()

            return redirect("ap-inicio")
        else:
            return render(request, "appSitio/agregar_avatar.html", {"form": formulario, "errors": formulario.errors})
    formulario = AvatarForm()

    return render(request, "appSitio/agregar_avatar.html", {"form": formulario})
