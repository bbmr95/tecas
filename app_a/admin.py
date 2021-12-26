from django.contrib import admin
from .models import Album, Libro, Pelicula

# Register your models here.
admin.site.register(Album)
admin.site.register(Libro)
admin.site.register(Pelicula)