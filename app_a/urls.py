from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('about/', views.sobre_mi, name = 'sobre_mi'),
    path('', views.index, name = 'index'),
    path('pages/', views.listas, name = 'lista'),
    
    path('lista_album/', views.AlbumListView.as_view(), name='lista_album'),
    path('crear_album/', views.AlbumCreateView.as_view(), name='crear_album'),
    path('eliminar_album/<int:pk>', views.AlbumDeleteView.as_view(), name='eliminar_album'),
    path('detalle_album/<int:pk>', views.AlbumDetailView.as_view(), name='detalle_album'),
    path('editar_album/<int:pk>', views.AlbumEditView.as_view(), name='editar_album'),
    path('buscar_album/', views.busquedaAlbum, name='buscar_album'),
    
    path('lista_libro/', views.LibroListView.as_view(), name='lista_libro'),
    path('crear_libro/', views.LibroCreateView.as_view(), name='crear_libro'),
    path('eliminar_libro/<int:pk>', views.LibroDeleteView.as_view(), name='eliminar_libro'),
    path('detalle_libro/<int:pk>', views.LibroDetailView.as_view(), name='detalle_libro'),
    path('editar_libro/<int:pk>', views.LibroEditView.as_view(), name='editar_libro'),
    path('buscar_libro/', views.busquedaLibro, name='buscar_libro'),
    
    path('lista_pelicula/', views.PeliculaListView.as_view(), name='lista_pelicula'),
    path('crear_pelicula/', views.PeliculaCreateView.as_view(), name='crear_pelicula'),
    path('eliminar_pelicula/<int:pk>', views.PeliculaDeleteView.as_view(), name='eliminar_pelicula'),
    path('detalle_pelicula/<int:pk>', views.PeliculaDetailView.as_view(), name='detalle_pelicula'),
    path('editar_pelicula/<int:pk>', views.PeliculaEditView.as_view(), name='editar_pelicula'),
    path('buscar_pelicula/', views.busquedaPelicula, name='buscar_pelicula'),
    
    path('login/', views.login_req, name = 'login'),
    path('login_fail/', views.login_fail, name = 'login_fail'),
    path('logout/', LogoutView.as_view(template_name='tem/logout.html'), name = 'logout'),
    path('registro/', views.registro_req, name = 'registro'),
    path('editar_user/', views.editar_usuario, name = 'editar'),
    path('info_usuario/', views.info_usuario, name = 'info_usuario')
    #path('editar_avatar/', views.editar_avatar, name = 'editar_avatar')
]
