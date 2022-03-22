from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Banda, Musico, Recitales
from clase.forms import BusquedaBanda, BandaFormulario, MusicoFormulario, RecitalesFormulario


# Create your views here.


def nueva_banda(request):
    nueva_banda = Banda(nombre= "banda")
    nueva_banda.save()
    return HttpResponse(f"se creó la banda {nueva_banda.nombre}")


def formulario_banda(request):
 
  
    if request.method == 'POST':
        formulario = BandaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_banda = Banda(nombre=data['Banda'], ciudad=data['ciudad'])
            nueva_banda.save()
            return render(request, 'indice/index.html', {'nueva_banda': nueva_banda})
            
    formulario = BandaFormulario()
    return render(request, 'clase/formulario_banda.html', {'formulario': formulario})

def formulario_musico(request):
 
  
    if request.method == 'POST':
        formulario = MusicoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_musico = Musico(nombre=data['Nombre'], instrumento=data['Instrumento'])
            nuevo_musico.save()
            return render(request, 'indice/index.html', {'nuevo_musico': nuevo_musico})
            
    formulario = MusicoFormulario()
    return render(request, 'clase/formulario_musico.html', {'formulario': formulario})

def formulario_recitales(request):

    
    if request.method == 'POST':
        formulario = RecitalesFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_recital = Recitales(nombre=data['recital'], ciudad=data['ciudad'])
            nuevo_recital.save()
            return render(request, 'indice/index.html', {'nuevo_recital': nuevo_recital})
            
    formulario = BandaFormulario()
    return render(request, 'clase/formulario_recitales.html', {'formulario': formulario})

def busqueda_banda(request):
    bandas_buscadas = []
    dato = request.GET.get('partial_banda', None)
    
    if dato is not None:
        bandas_buscadas = Banda.objects.filter(nombre__icontains=dato)
    
    buscador = BusquedaBanda()
    return render(
        request, "clase/busqueda_banda.html",
        {'buscador': buscador, 'bandas_buscadas': bandas_buscadas, 'dato': dato}
    )
    