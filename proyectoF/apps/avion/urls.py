from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='viajes'),
    path('crearAvion', views.crearAvion, name='crear_avion'),
    path('eliminarAvion/<int:numero>/', views.eliminarAvion, name='eliminar_avion'),
    path('clientes/<int:numero>/', views.listarClientes, name="clientes"),
]