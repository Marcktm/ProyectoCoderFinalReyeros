from django import forms

class ExperienciasForm(forms.Form):

    name = forms.CharField()
    fecha = forms.DateField()
    datos = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()