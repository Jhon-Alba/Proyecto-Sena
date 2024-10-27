# create_groups.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Create administrator and empleado groups'

    def handle(self, *args, **kwargs):
        # Crear grupo de Administradores
        admin_group, created = Group.objects.get_or_create(name='Administrador')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo "Administrador" creado exitosamente.'))
        else:
            self.stdout.write('El grupo "Administrador" ya existe.')

        # Crear grupo de Empleado
        operator_group, created = Group.objects.get_or_create(name='Empleado')
        if created:
            self.stdout.write(self.style.SUCCESS('Grupo "Empleado" creado exitosamente.'))
        else:
            self.stdout.write('El grupo "Empleado" ya existe.')

        # Agregar permisos al grupo "Administrador"
        admin_permissions = Permission.objects.filter(codename__in=['add_user', 'change_user', 'delete_user'])
        admin_group.permissions.set(admin_permissions)
        self.stdout.write('Permisos agregados al grupo "Administrador".')

        # Agregar permisos al grupo "Empleado"
        operator_permissions = Permission.objects.filter(codename__in=['view_user'])
        operator_group.permissions.set(operator_permissions)
        self.stdout.write('Permisos agregados al grupo "Empleado".')
