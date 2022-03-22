from django.urls import path
from .views import nueva_banda, formulario_banda, busqueda_banda, formulario_recitales, formulario_musico

urlpatterns = [
    path("nueva/", nueva_banda, name="nueva_banda"),
    path("banda/", formulario_banda, name="formulario_banda"),
    path("busqueda-banda/", busqueda_banda, name="busqueda_banda"),
    path("musico/", formulario_musico, name="formulario_musico"),
    path("recitales/", formulario_recitales, name="formulario_recitales"),
               
]