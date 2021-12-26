from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView 
from .models import Album, Libro, Pelicula

# Create your views here.
def sobre_mi(request):
    return render(request, 'tem/sobre_mi.html')

def index(request):
    return render(request, 'tem/index.html')

def login_req(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            if user is not None:
                login(request, user)
                return render(request, 'tem/index.html', {'mensaje':'Te logueste con éxito!'})
            else:
                return render(request, 'tem/login_fail.html', {'mensaje':'Error: Credenciales incorrectas', 'error':True})
        else:
            return render(request, 'tem/login_fail.html', {'mensaje':'Error: Los datos tienen mal formato', 'error':True})
            
    form = AuthenticationForm()
    
    return render(request, 'tem/login.html', {'form':form, 'mensaje':'', 'error':False})

def login_fail(request):
    return render(request, 'tem/login_fail.html')

def listas(request):
    return render(request, 'tem/lista.html')

class AlbumCreateView(CreateView):
    model = Album
    success_url = '/app_a/lista_album'
    fields = ['titulo','anio','autor','genero']
    template_name = 'album/crear_album.html'
    
class AlbumDeleteView(DeleteView):
    model = Album
    success_url = '/app_a/lista_album'
    template_name = 'album/borrar_album.html'

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album/detalle_album.html'

class AlbumListView(ListView):
    model = Album
    template_name = 'album/lista_album.html'


class LibroCreateView(CreateView):
    model = Libro
    success_url = '/app_a/lista_libro'
    fields = ['titulo','anio','autor','pais']
    template_name = 'libro/crear_libro.html'
    
class LibroDeleteView(DeleteView):
    model = Libro
    success_url = '/app_a/lista_libro'
    template_name = 'libro/borrar_libro.html'

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libro/detalle_libro.html'

class LibroListView(ListView):
    model = Libro
    template_name = 'libro/lista_libro.html'


class PeliculaCreateView(CreateView):
    model = Pelicula
    success_url = '/app_a/lista_pelicula'
    fields = ['titulo','anio','dir','dur']
    template_name = 'pelicula/crear_pelicula.html'
    
class PeliculaDeleteView(DeleteView):
    model = Pelicula
    success_url = '/app_a/lista_pelicula'
    template_name = 'pelicula/borrar_pelicula.html'

class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = 'pelicula/detalle_pelicula.html'

class PeliculaListView(ListView):
    model = Pelicula
    template_name = 'pelicula/lista_pelicula.html'