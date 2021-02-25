from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import FormularioLogin

# Create your views here.
def autenticar(request):
    if request.method == 'POST':
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']
            user = authenticate(username = usuario, password=clave)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('homepage'))
                else:
                    return HttpResponseRedirect(reverse('no_activo'))

    else:    
        formulario = FormularioLogin()
    context = {
        'formulario': formulario
    }
    return render (request, 'login/login.html', context) 
def desautenticar(request):
    return redirect (request, '/')

def welcome (request):
    return (request, 'login/welcome.html')

def forbidden (request):
    return (request, 'login/forbidden.html') 

def desactivado (request):
    return (request, 'login/deactive.html')  