from django.db import models

# Create your models here.
class Videojuegos(models.Model):
    id_videojuego = models.IntegerField(null=False, primary_key=True)
    titulo = models.CharField(max_length=100,null=False)
    genero = models.CharField(max_length=100,null=False)
    plataforma = models.CharField(max_length=100, null=False)
    precio= models.IntegerField(null=False)
    stock = models.IntegerField(null=False)
    fecha_lanzamiento = models.DateField()