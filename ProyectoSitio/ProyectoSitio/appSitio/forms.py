from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MadreFormulario(forms.Form):
    nombre = forms.CharField(max_length = 50)
    edad = forms.IntegerField()
    peso = forms.FloatField()
    datos = forms.CharField(widget=forms.Textarea)

class BebeFormulario(forms.Form):

    dia = forms.IntegerField()
    mes = forms.IntegerField()
    year = forms.IntegerField()

class SemanaFormulario(forms.Form):
    
    semana = forms.IntegerField()
    datos = forms.CharField(widget=forms.Textarea)

class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label = "correo electonico")
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repeat password", widget=forms.PasswordInput)
    
    class Meta():

        model = User
        fields = ["username", "email", "last_name", "password1", "password2"]

class UserEditForm(UserCreationForm):
    last_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label = "correo electonico")
    password1 = forms.CharField(label="password", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="repeat password", widget=forms.PasswordInput, required=False)
    class Meta():

        model = User
        fields = ["email", "last_name"]
        

        help_text = { k:"" for k in fields }

class AvatarForm(forms.Form):
     imagen = forms.ImageField()


