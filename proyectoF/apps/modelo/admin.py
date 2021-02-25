from django.contrib import admin
from .models import Cliente
from .models import Viaje
from .models import Avion

admin.site.register(Cliente)
admin.site.register(Viaje)
admin.site.register(Avion)