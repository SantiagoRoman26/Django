from django.shortcuts import render
from apps.modelo.models import Avion,Cliente
from .forms import FormularioAvion
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User  
from django.db.models import Q 
# Create your views here.

@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name = "avion").exists():
        listaAvion = Avion.objects.all() 
        busqueda = request.POST.get("busqueda")
        if busqueda:
            listaAvion = Avion.objects.filter(
                Q(numero__icontains = busqueda) | 
                Q(destino__icontains = busqueda) 
            ).distinct() 
        return render (request, 'aviones/index_Todos.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals()) 

@login_required
def crearAvion(request):
    formulario_avion = FormularioAvion(request.POST)
    if request.method == 'POST':
        if formulario_avion.is_valid():

            avion = Avion()
            datos_avion = formulario_avion.cleaned_data
            avion.numero = datos_avion.get('numero')
            avion.capacidad= datos_avion.get('capacidad')
            avion.puestos_Disponibles= avion.capacidad
            #ORM
            
            avion.save()

        return redirect(index)
    return render (request, 'aviones/crear.html', locals())
def eliminarAvion(request, numero):
    avion = Avion.objects.get(numero=numero)
    avion.delete()
    return redirect(index)

def listarClientes(request, numero):
    avion = Avion.objects.get(numero=numero)
    cliente = Cliente.objects.filter(avion=avion)
    return render(request, 'clientes/index.html', locals())