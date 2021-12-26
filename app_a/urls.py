from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.sobre_mi, name = 'sobre_mi'),
    path('index/', views.index, name = 'index'),
    path('login/', views.login_req, name = 'login'),
    path('login_fail/', views.login_fail, name = 'login_fail'),
    path('pages/', views.listas, name = 'lista'),
    
    path('lista_album/', views.AlbumListView.as_view(), name='lista_album'),
    path('crear_album/', views.AlbumCreateView.as_view(), name='crear_album'),
    path('eliminar_album/<int:pk>', views.AlbumDeleteView.as_view(), name='eliminar_album'),
    path('detalle_album/<int:pk>', views.AlbumDetailView.as_view(), name='detalle_album'),
    
    path('lista_libro/', views.LibroListView.as_view(), name='lista_libro'),
    path('crear_libro/', views.LibroCreateView.as_view(), name='crear_libro'),
    path('eliminar_libro/<int:pk>', views.LibroDeleteView.as_view(), name='eliminar_libro'),
    path('detalle_libro/<int:pk>', views.LibroDetailView.as_view(), name='detalle_libro'),
    
    path('lista_pelicula/', views.PeliculaListView.as_view(), name='lista_pelicula'),
    path('crear_pelicula/', views.PeliculaCreateView.as_view(), name='crear_pelicula'),
    path('eliminar_pelicula/<int:pk>', views.PeliculaDeleteView.as_view(), name='eliminar_pelicula'),
    path('detalle_pelicula/<int:pk>', views.PeliculaDetailView.as_view(), name='detalle_pelicula')
]
