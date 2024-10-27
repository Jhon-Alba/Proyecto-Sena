from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from models import *

class Command(BaseCommand):
    help = 'Assign permissions to the Operator group for Venta and Factura models'

    def handle(self, *args, **kwargs):
        # Obtener el grupo Operador
        operador_group = Group.objects.get(name='Operador')

        # Obtener los ContentTypes de los modelos Venta y Factura
        venta_ct = ContentType.objects.get_for_model(venta)
        compra_ct = ContentType.objects.get_for_model(compra)

        # Obtener los permisos para los modelos Venta y Factura
        permisos_venta = Permission.objects.filter(content_type=venta_ct)
        permisos_compra = Permission.objects.filter(content_type=compra_ct)

        # Asignar permisos al grupo Operador
        operador_group.permissions.set(permisos_venta | permisos_compra)

        self.stdout.write(self.style.SUCCESS("Permisos asignados al grupo Operador para los modelos Venta y Factura."))