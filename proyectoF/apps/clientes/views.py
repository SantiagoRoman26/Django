from django.shortcuts import render
from apps.modelo.models import Cliente
from .forms import FormularioCliente
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User  
from django.db.models import Q 
# Create your views here.

@login_required
def index(request):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_aereopuerto").exists():
        listaClientes = Cliente.objects.all() 
        busqueda = request.POST.get("busqueda")
        if busqueda:
            listaClientes = Cliente.objects.filter(
                Q(cedula__icontains = busqueda) | 
                Q(apellidos__icontains = busqueda) | 
                Q(nombres__icontains = busqueda) 
            ).distinct() 
        return render (request, 'clientes/index_Todos.html', locals())
    else:
        return render(request, 'login/forbidden.html', locals()) 


@login_required
def crearCliente(request):
    formulario_cliente = FormularioCliente(request.POST)
    if request.method == 'POST':
        if formulario_cliente.is_valid():
            cliente = Cliente()
            datos_cliente = formulario_cliente.cleaned_data
            cliente.cedula = datos_cliente.get('cedula')
            cliente.apellidos= datos_cliente.get('apellidos')
            cliente.nombres= datos_cliente.get('nombres')
            cliente.genero= datos_cliente.get('genero')
            cliente.correo= datos_cliente.get('correo')
            cliente.celular= datos_cliente.get('celular')
            cliente.avion= datos_cliente.get('avion')
            avion=cliente.avion
            if avion.puestos_Disponibles==0:
                return redirect(index)
            else:
                avion.puestos_Disponibles=avion.puestos_Disponibles-1
                if avion.puestos_Disponibles==0:
                    avion.estado=False
                #ORM
            
                cliente.save()
                avion.save()
            
        return redirect(index)
    return render (request, 'clientes/crear.html', locals())
def eliminarCliente(request, cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    avion=cliente.avion
    if avion.estado==False:
        avion.estado=True
    avion.puestos_Disponibles=avion.puestos_Disponibles+1
    cliente.delete()
    avion.save()
    return redirect(index)

def modificarCliente(request, cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    if request.method == 'GET':
        formulario_cliente = FormularioCliente(instance = cliente)
    else:
        formulario_cliente = FormularioCliente(request.POST, instance = viaje)
        if formulario_cliente.is_valid():
            #ORM
            formulario_cliente.save()
        return redirect(index)
    return render (request, 'clientes/modificar.html', locals())