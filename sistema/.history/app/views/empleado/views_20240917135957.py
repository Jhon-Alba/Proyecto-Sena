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

@method_decorator(login_required, name='dispatch')
class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/crear.html'
    success_url = reverse_lazy('empleado_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar empleado'
        context['entidad'] = 'Registrar empleado'
        context['listar_url'] = reverse_lazy('empleado_lista')
        context['has_permission'] = not self.request.user.groups.filter(name='Empleado').exists() and self.request.user.has_perm('app.add_empleado')
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('app.add_empleado') or self.request.user.groups.filter(name='Empleado').exists():
            return redirect('empleado_lista')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)
        
        
        
        

@method_decorator(login_required, name='dispatch')
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/crear.html'
    success_url = reverse_lazy('empleado_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Empleado'
        context['entidad'] = 'Empleado'
        context['listar_url'] = reverse_lazy('empleado_lista')
        context['has_permission'] = not self.request.user.groups.filter(name='Empleado').exists() and self.request.user.has_perm('app.change_empleado')
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('app.change_empleado') or self.request.user.groups.filter(name='Empleado').exists():
            return redirect('empleado_lista')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)
    

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