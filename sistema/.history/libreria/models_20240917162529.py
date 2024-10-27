
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.validators import MinLengthValidator
from .choices import codigos_telefonicos_paises
from django.db import models



from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Respaldo(models.Model):
    nombre_archivo = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tamano = models.FloatField()

    def str(self):
        return self.nombre_archivo


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    activado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    activado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Presentacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    activado = models.BooleanField(default=True)


    def __str__(self):
        return self.nombre


class UnidadMedida(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    activado = models.BooleanField(default=True)


    def __str__(self):
        return self.nombre



class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='producto', verbose_name='Categoria', null=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='producto', verbose_name='Marca', null=True)
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE, related_name='producto', verbose_name='Presentacion', null=True)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, related_name='producto', verbose_name='UnidadMedida', null=True)
    activado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    numero_celular = models.BigIntegerField(verbose_name='Número de Celular')
    correo_electronico = models.EmailField(max_length=100, verbose_name='Correo Electrónico')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='proveedores', verbose_name='Nombre de marca', null=True)
    activado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    


#COMPRA
        
class compra(models.Model):

    producto
    nombreproducto = models.CharField(max_length=100)
    fechaingreso = models.DateField()  
    cantidad = models.IntegerField()
    valorunitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valortotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    activado = models.BooleanField(default=True)
    
    def _str_(self):
        return self.nombreproducto

#VENTA
class venta(models.Model):

    nombreproducto = models.CharField(max_length=100)
    fechaventa = models.DateField()  
    cantidad = models.IntegerField()
    valorunitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valortotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    activado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombreproducto



