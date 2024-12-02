from django.urls import path
from videojuegos_app import views
urlpatterns = [
    path("", views.inicio_vistaVideojuegos, name= "inicio_vistaVideojuegos" ),
    path("registrarVideojuegos/",views.registrarVideojuegos,name="registrarVideojuegos"),
    path("seleccionarVideojuegos/<id_videojuego>",views.seleccionarVideojuegos,name="seleccionarVideojuegos"),
    path("editarVideojuegos/",views.editarVideojuegos,name="editarVideojuegos"),
    path("borrarVideojuegos/<id_videojuego>",views.borrarVideojuegos,name="borrarVideojuegos")
]