from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.validators import MinLengthValidator


class Administrador(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'CC', 'Cédula de Ciudadanía'
        CE = 'CE', 'Cédula de Extranjería'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='administrador')
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Número de documento", unique=True)
    telefono = models.PositiveIntegerField(verbose_name="Teléfono")
    contrasena = models.CharField(max_length=128, validators=[MinLengthValidator(8)], verbose_name="Contraseña")
    conf_contrasena = models.CharField(max_length=128, verbose_name="Confirmación de contraseña", default="")
    activado = models.BooleanField(default=True, verbose_name="Activado")


    @staticmethod
    def validar_numero_documento(value):
     if value is None:
        return  
     if value < 10000000 or value > 9999999999:
        raise ValidationError("El número de documento debe tener entre 8 y 10 dígitos.")


    @staticmethod
    def validar_telefono(value):
        if value is None:
         return 
        if value < 1000000 or value > 9999999999:
         raise ValidationError("El teléfono debe tener entre 7 y 10 dígitos.")

    def clean(self):
        
        self.validar_numero_documento(self.numero_documento)
        self.validar_telefono(self.telefono)
        
        
        super().clean()
        if self.contrasena != self.conf_contrasena:
            raise ValidationError({"conf_contrasena": "Las contraseñas no coinciden."})

    def save(self, *args, **kwargs):
        if not self.pk or 'user' not in kwargs:
            user, created = User.objects.get_or_create(username=self.user.username)
        else:
            user = self.user

        if self.contrasena:
            user.set_password(self.contrasena)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        self.user = user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        db_table = 'administrador'

@receiver(post_delete, sender=Administrador)
def eliminar_usuario_relacionado(sender, instance, **kwargs):
    user = instance.user
    if user:
        user.delete()

########################################################################################################################################

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, ValidationError
from django.dispatch import receiver
from django.db.models.signals import post_delete

class Empleado(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'CC', 'Cédula de Ciudadanía'
        TI = 'TI', 'Tarjeta de Identidad'
        CE = 'CE', 'Cédula de Extranjería'
        PSP = 'PSP', 'Pasaporte'

    def validar_numero_documento(value):
        if not (10000000 <= value <= 9999999999):
            raise ValidationError("El número de documento debe tener entre 8 y 10 dígitos.")

    def validar_telefono(value):
        if len(str(value)) != 10:  # Verifica que el número de teléfono tenga exactamente 10 dígitos
            raise ValidationError("El número de teléfono debe tener exactamente 10 dígitos.")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empleado')
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveBigIntegerField(verbose_name="Número de documento", unique=True, validators=[validar_numero_documento])
    telefono = models.CharField(max_length=10, verbose_name="Teléfono", validators=[validar_telefono])
    contrasena = models.CharField(max_length=128, validators=[MinLengthValidator(8)], verbose_name="Contraseña")
    conf_contrasena = models.CharField(max_length=128, verbose_name="Confirmación de contraseña", default="")
    activado = models.BooleanField(default=True, verbose_name="Activado")
      
    def clean(self):
        super().clean()
        if self.contrasena != self.conf_contrasena:
            raise ValidationError({"conf_contrasena": "Las contraseñas no coinciden."})

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        db_table = 'Empleado'

@receiver(post_delete, sender=Empleado)
def eliminar_usuario_relacionado(sender, instance, **kwargs):
    user = instance.user
    if user:
        user.delete()
