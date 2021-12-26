from django.db import models

# Create your models here.
class Album(models.Model):
    titulo = models.CharField(max_length=100)
    anio = models.IntegerField()
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.autor} - {self.titulo} ({self.anio})'

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    anio = models.IntegerField()
    autor = models.CharField(max_length=100)
    pais = models.CharField(max_length=60)
    
    def __str__(self):
        return f'{self.autor} - {self.titulo} ({self.anio})'
    
class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    anio = models.IntegerField()
    dir = models.CharField(max_length=100)
    dur = models.IntegerField()
    
    def __str__(self):
        return f'{self.dir} - {self.titulo} ({self.anio})'