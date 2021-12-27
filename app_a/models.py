from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Album(models.Model):
    titulo = models.CharField(max_length=100)
    anio = models.IntegerField()
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    portada = models.ImageField(upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.autor} - {self.titulo} ({self.anio})'

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    anio = models.IntegerField()
    autor = models.CharField(max_length=100)
    pais = models.CharField(max_length=60)
    portada = models.ImageField(upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.autor} - {self.titulo} ({self.anio})'
    
class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    anio = models.IntegerField()
    dir = models.CharField(max_length=100)
    dur = models.IntegerField()
    portada = models.ImageField(upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.dir} - {self.titulo} ({self.anio})'


# class Avatar(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

