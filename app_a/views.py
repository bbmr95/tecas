from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView 

from .models import Album, Libro, Pelicula, Avatar
from .forms import FormularioAlbum, FormularioPelicula, FormularioLibro, RegistroUsuario, EditarUsuario, AvatarForm



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

def registro_req(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, 'tem/index.html', {'tiene_mensaje': True, 'mensaje': f'Se creo el {usuario}'})
        
    form = RegistroUsuario()
    return render(request, 'tem/registro.html', {'form': form, 'mensaje': '', 'error': False})

@login_required
def editar_usuario(request):
    usuario = request.user
    
    if request.method == 'POST':
        form = EditarUsuario(request.POST)
        
        if form.is_valid():
            datos = form.cleaned_data
            
            usuario.email = datos['email']
            usuario.password1 = datos['password1']
            usuario.password2 = datos['password2']
            usuario.first_name = datos['first_name']
            usuario.last_name = datos['last_name']
            
            usuario.save()
            
            return render(request, 'tem/index.html', {'tiene_mensaje':True, 'mensaje': f'Se edito correctamente'})
    else:
        form = EditarUsuario(initial={'first_name': usuario.first_name, 'last_name': usuario.last_name, 'email': usuario.email})
    
    return render(request, 'tem/editar_usuario.html', {'form': form})

@login_required
def editar_avatar(request):
    usuario = request.user
    
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid():
            avatar = Avatar.object.get(user=usuario)
            avatar.avatar = form.cleaned_data['avatar']
            avatar.save()
            
            return render(request, 'tem/index.html',
                          {'tiene_mensaje':True, 'mensaje':f'Se cargo correctamente el avatar', 'url_avatar': avatar.avatar.url})
    else:
        form = AvatarForm()
    
    return render(request, 'tem/editar_avatar.html', {'form':form})
            

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