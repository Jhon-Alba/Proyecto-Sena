from django.urls import path
from app.views import *
from app.views.administrador.views import *
from app.views.empleado.views import *



app_name = 'app'
urlpatterns = [

    path('administrador/', administrador_list, name='administrador_lista'),
    path('administrador/crear/', administrador_create, name='administrador_crear'),
    path('administrador/editar/<int:id>/', administrador_update, name='administrador_editar'),
    path('administrador/eliminar/<int:id>/', administrador_delete, name='eliminar_administrador'),
    path('reportes/administradores/pdf/', reporte_administradores_pdf, name='reporte_administradores_pdf'),
    path('reportes/administradores/excel/', reporte_administradores_excel, name='reporte_administradores_excel'),
    path('administrador/activar/<int:pk>/', activar_administrador, name='activar_administrador'),
    path('administrador/desactivar/<int:pk>/', desactivar_administrador, name='desactivar_administrador'),


    ### CRUD Empleado ###
    path('listar/', empleado_list, name='empleado_lista'),
    path('crear/', empleado_create, name='empleado_crear'),
    path('editar/<int:id>/', empleado_update, name='empleado_editar'),
    path('eliminar/<int:id>/', empleado_delete, name='empleado_eliminar'),
    path('activar/<int:pk>/', activar_empleado, name='empleado_activar'),
    path('desactivar/<int:pk>/', desactivar_empleado, name='empleado_desactivar'),
    path('reporte/excel/', reporte_empleados_excel, name='reporte_empleados_excel'),
    path('reporte/pdf/', reporte_empleados_pdf, name='reporte_empleados_pdf'),

   
]

