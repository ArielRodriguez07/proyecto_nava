from django.shortcuts import render, redirect
from .models import Videojuegos
# Create your views here.
def inicio_vistaVideojuegos(request):
    losVideojuegos=Videojuegos.objects.all()
    return render(request,"gestionarVideojuegos.html", {"misvideojuegos":losVideojuegos}   )

def registrarVideojuegos(request):
    id_videojuego=request.POST["numid_videojuego"]
    titulo=request.POST["txttitulo"]
    genero=request.POST["txtgenero"]
    plataforma=request.POST["txtplataforma"]
    precio=request.POST["numprecio"]
    stock=request.POST["numstock"]
    fecha_lanzamiento=request.POST["datfecha_lanzamiento"]
    
    guardarVideojuegos=Videojuegos.objects.create(
        id_videojuego=id_videojuego,titulo=titulo,genero=genero,plataforma=plataforma,precio=precio,stock=stock,fecha_lanzamiento=fecha_lanzamiento
    ) #GUARDA EL REGISTRO
    
    return redirect("/")

def seleccionarVideojuegos(request,id_videojuego):
    videojuegos=Videojuegos.objects.get(id_videojuego=id_videojuego)
    return render(request, "editarVideojuegos.html",{"misVideojuegos":videojuegos})

def editarVideojuegos(request):
    id_videojuego=request.POST["numid_videojuego"]
    titulo=request.POST["txttitulo"]
    genero=request.POST["txtgenero"]
    plataforma=request.POST["txtplataforma"]
    precio=request.POST["numprecio"]
    stock=request.POST["numstock"]
    fecha_lanzamiento=request.POST["datfecha_lanzamiento"]
    videojuegos=Videojuegos.objects.get(id_videojuego=id_videojuego)
    videojuegos.titulo=titulo
    videojuegos.genero=genero
    videojuegos.plataforma=plataforma
    videojuegos.precio=precio
    videojuegos.stock=stock
    videojuegos.fecha_lanzamiento=fecha_lanzamiento
    
    videojuegos.save() #guarda registro actualizado
    return redirect("/")

def borrarVideojuegos(request,id_videojuego):
    videojuegos=Videojuegos.objects.get(id_videojuego=id_videojuego)
    videojuegos.delete() # borra el registro
    return redirect("/")