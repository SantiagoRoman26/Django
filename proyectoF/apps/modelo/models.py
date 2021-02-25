from django.db import models
class Avion(models.Model):
    avion_id = models.AutoField(primary_key = True)
    numero = models.CharField(max_length = 20, unique = True, null = False)
    capacidad = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    puestos_Disponibles=models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    estado = models.BooleanField(default = True)
    def __str__(self):
        
        return self.numero

class Cliente(models.Model):

    listaGenero = (
        ('femenino','Femenino'),
        ('masculino', 'Masculino')
    )

    cliente_id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length = 10, unique = True, null = False)
    nombres = models.CharField(max_length = 70, null = False)
    apellidos = models.CharField(max_length = 70, null = False)
    genero = models.CharField(max_length = 30, choices = listaGenero, default = 'masculino')
    correo = models.EmailField(max_length = 105, null = False)
    celular = models.CharField(max_length = 15, null = False)
    avion = models.ForeignKey(Avion, on_delete = models.CASCADE) 
    date_created = models.DateTimeField(auto_now_add = True)
    

    def __str__ (self):
        return self.cedula



class Viaje(models.Model):

    viaje_id = models.AutoField(primary_key = True)
    numero = models.CharField(max_length = 20, unique = True, null = False)
    fechaViaje = models.DateTimeField()
    fechaLlegada = models.DateTimeField()
    destino = models.CharField(max_length = 70, null = False)
    avion = models.ForeignKey(Avion, on_delete = models.CASCADE) 
    estado = models.BooleanField(default = True)
    
         
    def __str__(self):
        
        return self.numero