
from django.http import HttpResponse
import random
from django.template import loader
from django.shortcuts import render

def inicio(request):
    return render(request, "indice/index.html", {})

def otra_vista(request):
    return HttpResponse('''
                        <h1>Este es un titulo en h1</h1>
                        ''')

def numero_random(request):
    numero = random.randrange(100,2000)
    return HttpResponse(numero)


def numero_usuario(request, numero):
    texto = f'<h1>El numero es: {numero}</h1>'
    return HttpResponse(texto)

def mi_plantilla(request):
     
    return render(request, "indice/mi_plantilla.html")