from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.core.exceptions import ValidationError
from app.models import Empleado
from app.forms import EmpleadoForm

@never_cache
@login_required
def empleado_list(request):
    if not request.user.has_perm('app.view_empleado'):
        return render(request, 'empleado/listar.html', {'has_permission': False})

    empleados = Empleado.objects.all()

    estado_filtro = request.GET.get('estado', None)
    buscar_nombre = request.GET.get('buscar_nombre', '')
    buscar_telefono = request.GET.get('buscar_telefono', '')

    if estado_filtro == 'activado':
        empleados = empleados.filter(activado=True)
    elif estado_filtro == 'inactivado':
        empleados = empleados.filter(activado=False)

    if buscar_nombre:
        empleados = empleados.filter(nombre__icontains=buscar_nombre)

    if buscar_telefono:
        empleados = empleados.filter(telefono__icontains=buscar_telefono)

    breadcrumbs = [
        {'name': 'Inicio', 'url': '/dashboard'},
        {'name': 'Empleados', 'url': '/app/empleado/listar/'},
    ]

    context = {
        'titulo': 'Listado de empleados',
        'entidad': 'Empleados',
        'listar_url': reverse_lazy('empleado_lista'),
        'crear_url': reverse_lazy('empleado_crear'),
        'empleados': empleados,
        'breadcrumbs': breadcrumbs,
        'has_permission': request.user.has_perm('app.view_empleado'),
        'can_add': request.user.has_perm('app.add_empleado') and not request.user.groups.filter(name='Empleado').exists(),
    }
    return render(request, 'empleado/listar.html', context)



@never_cache
@login_required
def empleado_create(request):
    if not request.user.has_perm('app.add_empleado') or request.user.groups.filter(name='Empleado').exists():
        return redirect('empleado_lista')

    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, '¡Empleado creado con éxito!')
                return redirect('empleado_lista')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = EmpleadoForm()

    breadcrumbs = [
        {'name': 'Inicio', 'url': '/dashboard'},
        {'name': 'Empleados', 'url': '/app/empleado/listar/'},
        {'name': 'Registrar Empleado', 'url': '/app/empleado/crear/'},
    ]

    context = {
        'titulo': 'Registrar empleado',
        'entidad': 'Registrar empleado',
        'listar_url': reverse_lazy('empleado_lista'),
        'form': form,
        'breadcrumbs': breadcrumbs,
        'has_permission': not request.user.groups.filter(name='Empleado').exists() and request.user.has_perm('app.add_empleado'),
    }
    return render(request, 'empleado/crear.html', context)


@never_cache
@login_required
def empleado_update(request, id):
    if not request.user.has_perm('app.change_empleado') or request.user.groups.filter(name='Empleado').exists():
        return redirect('empleado_lista')

    empleado = get_object_or_404(Empleado, id=id)

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, '¡Empleado editado con éxito!')
                return redirect('empleado_lista')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = EmpleadoForm(instance=empleado)

    breadcrumbs = [
        {'name': 'Inicio', 'url': '/dashboard'},
        {'name': 'Empleados', 'url': '/app/empleado/listar/'},
        {'name': 'Editar Empleado', 'url': f'/app/empleado/editar/{id}/'},
    ]

    context = {
        'titulo': 'Editar empleado',
        'entidad': 'Empleado',
        'listar_url': reverse_lazy('empleado_lista'),
        'form': form,
        'breadcrumbs': breadcrumbs,
        'has_permission': request.user.has_perm('app.change_empleado') and not request.user.groups.filter(name='Empleado').exists(),
    }

    return render(request, 'empleado/crear.html', context)



@method_decorator(login_required, name='dispatch')
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado/eliminar.html'
    success_url = reverse_lazy('empleado_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar empleado'
        context['entidad'] = 'Eliminar empleado'
        context['listar_url'] = reverse_lazy('empleado_lista')
        context['has_permission'] = not self.request.user.groups.filter(name='Empleado').exists() and self.request.user.has_perm('app.delete_empleado')
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('app.delete_empleado') or self.request.user.groups.filter(name='Empleado').exists():
            return redirect('empleado_lista')
        return super().dispatch(request, *args, **kwargs)

class ActivarEmpleadoView(View):
    def get(self, request, pk, *args, **kwargs):
        empleado = get_object_or_404(Empleado, pk=pk)
        empleado.activado = True
        empleado.save()
        return redirect('empleado_lista')

class DesactivarEmpleadoView(View):
    def get(self, request, pk, *args, **kwargs):
        empleado = get_object_or_404(Empleado, pk=pk)
        empleado.activado = False
        empleado.save()
        return redirect('empleado_lista')