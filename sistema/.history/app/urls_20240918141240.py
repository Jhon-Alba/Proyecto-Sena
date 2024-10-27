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
     path('empleado/', empleado_list, name='empleado_lista'),
    path('empleado/reporte/excel/', reporte_empleados_excel, name='reporte_empleados_excel'),
    path('empleado/reporte/pdf/', reporte_empleados_pdf, name='reporte_empleados_pdf'),
    
    ### CRUD Empleado ###
    path('listar/', empleado_list, name='empleado_lista'),
    path('crear/', views.empleado_create, name='empleado_crear'),
    path('editar/<int:pk>/', views.empleado_update, name='empleado_editar'),
    path('eliminar/<int:pk>/', views.empleado_delete, name='eliminar_empleado'),
    path('activar/<int:pk>/', views.activar_empleado, name='activar_empleado'),
    path('desactivar/<int:pk>/', views.desactivar_empleado, name='desactivar_empleado'),

   
]

