
from django.db import models

#Tabla Usuario
class Usuario(models.Model):
    #Cuenta
    password        = models.CharField(max_length=128)
    username        = models.CharField(unique=True, max_length=150)
    #Datos Basicos
    nombr           = models.CharField(max_length=30)
    apell           = models.CharField(max_length=150)
    email           = models.CharField(max_length=254)
    #Tipo de usuario
    es_admin        = models.BooleanField(default=False)
    es_maest        = models.BooleanField(default=False)
    es_activ        = models.BooleanField(default=True)
    #Registro de actividad
    fecha_ingre     = models.DateTimeField(auto_now_add=True)
    fecha_conex     = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

