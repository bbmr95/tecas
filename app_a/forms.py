from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class FormularioAlbum(forms.Form):
    titulo = forms.CharField()
    anio = forms.IntegerField()
    autor = forms.CharField()
    genero = forms.CharField()

class FormularioLibro(forms.Form):
    titulo = forms.CharField()
    anio = forms.IntegerField()
    autor = forms.CharField()
    pais = forms.CharField()

class FormularioPelicula(forms.Form):
    titulo = forms.CharField()
    anio = forms.IntegerField()
    dir = forms.CharField()
    dur = forms.IntegerField()