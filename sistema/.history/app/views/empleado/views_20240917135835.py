from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.core.exceptions import ValidationError
from app.models import Empleado
from app.forms import EmpleadoForm

@method_decorator(login_required, name='dispatch')
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleado/index.html'
    context_object_name = 'empleados'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de empleados'
        context['entidad'] = 'Empleados'
        context['listar_url'] = reverse_lazy('empleado_lista')
        context['crear_url'] = reverse_lazy('empleado_crear')
        context['has_permission'] = self.request.user.has_perm('app.view_empleado')

        if self.request.user.groups.filter(name='Empleado').exists():
            context['can_add'] = False
        else:
            context['can_add'] = self.request.user.has_perm('app.add_empleado')
        
        estado_filtro = self.request.GET.get('estado', None)
        buscar_nombre = self.request.GET.get('buscar_nombre', '')
        buscar_telefono = self.request.GET.get('buscar_telefono', '')
        empleados = self.get_queryset()

        if estado_filtro == 'activado':
            empleados = empleados.filter(activado=True)
        elif estado_filtro == 'inactivado':
            empleados = empleados.filter(activado=False)

        if buscar_nombre:
            empleados = empleados.filter(nombre__icontains=buscar_nombre)

        if buscar_telefono:
            empleados = empleados.filter(telefono__icontains=buscar_telefono)

        context['empleados'] = empleados
        context['estado_filtro'] = estado_filtro
        context['buscar_nombre'] = buscar_nombre
        context['buscar_telefono'] = buscar_telefono
        
        return context

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