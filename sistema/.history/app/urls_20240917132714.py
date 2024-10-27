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
    path('empleado/listar/', EmpleadoListView.as_view(), name='empleado_lista'),
    path('empleado/crear/', EmpleadoCreateView.as_view(), name='empleado_crear'),
    path('empleado/editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado_editar'),
    path('empleado/eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_eliminar'),

   
]

