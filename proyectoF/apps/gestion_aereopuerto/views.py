from django.shortcuts import render
from apps.modelo.models import Viaje,Avion
from .forms import FormularioViaje
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User  
from django.db.models import Q 
# Create your views here.

@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        listaViajes = Viaje.objects.all() 
        busqueda = request.POST.get("busqueda")
        if busqueda:
            listaViajes = Viaje.objects.filter(
                Q(numero__icontains = busqueda) | 
                Q(destino__icontains = busqueda) 
            ).distinct() 
        return render (request, 'viajes/index.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals()) 

@login_required
def crearViaje(request):
    formulario_viaje = FormularioViaje(request.POST)
    if request.method == 'POST':
        if formulario_viaje.is_valid():

            viaje = Viaje()
            datos_viaje = formulario_viaje.cleaned_data
            viaje.numero = datos_viaje.get('numero')
            viaje.destino= datos_viaje.get('destino')
            viaje.fechaViaje= datos_viaje.get('fechaViaje')
            viaje.fechaLlegada= datos_viaje.get('fechaLlegada')
            viaje.avion=datos_viaje.get('avion')
            #ORM
            
            viaje.save()

        return redirect(index)
    return render (request, 'viajes/crear.html', locals())

def modificarViaje(request, numero):
    viaje = Viaje.objects.get(numero=numero)
    if request.method == 'GET':
        formulario_viaje = FormularioViaje(instance = viaje)
    else:
        formulario_viaje = FormularioViaje(request.POST, instance = viaje)
        if formulario_viaje.is_valid():
            #ORM
            formulario_viaje.save()
        return redirect(index)
    return render (request, 'viajes/modificar.html', locals())
    
def eliminarViaje(request, numero):
    viaje = Viaje.objects.get(numero=numero)
    viaje.delete()
    return redirect(index)

def listarAviones(request, numero):
    viaje = Viaje.objects.get(numero=numero)
    avion = Avion.objects.filter(viaje=viaje)
    return render(request, 'aviones/index.html', locals())