from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class RegistroUsuario(UserCreationForm):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Constraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        help_text = {k: '' for k in fields}

class EditarUsuario(UserCreationForm):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Constraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password1', 'password2', 'email']
        help_text = {k: '' for k in fields}

class AvatarForm(forms.Form):
    avatar = forms.ImageField()
