from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from libreria.views import *
from .views import *

from app.views.administrador.views import *
from app.views.empleado.views import *


urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('registrarme/', views.registrarme, name='registrarme'),
    path('login/', loginFormView.as_view(), name='login'),
    path('logout/', logoutRedirect.as_view(), name='logout'),
    path('ayuda/', views.ayuda, name='ayuda'),

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
    path('empleado/crear/', empleado_create, name='empleado_crear'),
    path('empleado/editar/<int:id>/', empleado_update, name='empleado_editar'),
    path('empleado/eliminar/<int:id>/', empleado_delete, name='empleado_eliminar'),
    path('empleado/reporte/excel/', reporte_empleados_excel, name='reporte_empleados_excel'),
    path('empleado/reporte/pdf/', reporte_empleados_pdf, name='reporte_empleados_pdf'),



    ### CRUD Categorias ###
    path('categorias/crear_categorias', views.crear_categorias, name='crear_categorias'),
    path('categorias/editar_categorias/<pk>/', views.editar_categorias, name='editar_categorias'),
    path('categorias/eliminar_categorias/<pk>/', views.eliminar_categorias, name='eliminar_categorias'),

    ### CRUD Marcas ###
    path('marcas/crear_marcas/', views.crear_marcas, name='crear_marcas'),
    path('marcas/editar_marcas/<pk>/', views.editar_marcas, name='editar_marcas'),
    path('marcas/eliminar_marcas/<pk>/', views.eliminar_marcas, name='eliminar_marcas'),

    ### CRUD Presentaciones ###
    path('presentaciones/crear_presentaciones/', views.crear_presentaciones, name='crear_presentaciones'),
    path('presentaciones/editar_presentaciones/<pk>/', views.editar_presentaciones, name='editar_presentaciones'),
    path('presentaciones/eliminar_presentaciones/<pk>/', views.eliminar_presentaciones, name='eliminar_presentaciones'),

    ### CRUD Producto ###
    path('producto/crear_productos/', views.crear_productos, name='crear_productos'),
    path('producto/editar_productos/<pk>/', views.editar_productos, name='editar_productos'),
    path('producto/eliminar_productos/<pk>/', views.eliminar_productos, name='eliminar_productos'),

    ### CRUD Proveedores ###
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),

    ### CRUD Unidades de Medida ###
    path('unidades_medida/crear_unidades_medida/', views.crear_unidades_medida, name='crear_unidades_medida'),
    path('unidades_medida/editar_unidades_medida/<pk>/', views.editar_unidades_medida, name='editar_unidades_medida'),
    path('unidades_medida/eliminar_unidades_medida/<pk>/', views.eliminar_unidades_medida, name='eliminar_unidades_medida'),

    ### CRUD Compra ###
    path('compra/crear', views.crear_compra, name='crear_compra'),
    path('compra/editar/<int:id>/', views.editar_compra, name='editar_compra'),
    path('compra/eliminar/<int:id>/', views.eliminar_compra, name='eliminar_compra'),

    ### CRUD Venta ###
    path('venta/crear', views.crear_venta, name='crear_venta'),
    path('venta/editar/<int:id>/', views.editar_venta, name='editar_venta'),
    path('venta/eliminar/<int:id>/', views.eliminar_venta, name='eliminar_venta'),

  

    ### Rutas Generales ###
    path('categorias/', views.categorias, name='categorias'),
    path('marcas/', views.marcas, name='marcas'),
    path('presentaciones/', views.presentaciones, name='presentaciones'),
    path('producto/', views.producto, name='producto'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('unidades_medida/', views.unidades_medida, name='unidades_medida'),
    path('compra/', views.compras, name='compra'),
    path('venta/', views.ventas, name='venta'),

    ### Reportes ###
    path('reporte_pdf_categorias/', views.reporte_categorias_pdf, name='reporte_pdf_categorias'),
    path('reporte_excel_categorias/', views.reporte_categorias_excel, name='reporte_excel_categorias'),
    path('compra/reporte/pdf/', views.reporte_compras_pdf, name='reporte_compras_pdf'),
    path('compra/reporte_excel/', views.reporte_compras_excel, name='reporte_compras_excel'),
    path('reporte_marcas/', views.reporte_marcas_pdf, name='reporte_marcas'),
    path('reporte_marcas_excel/', views.reporte_marcas_excel, name='reporte_marcas_excel'),
    path('proveedores/reporte/pdf/', views.reporte_proveedores_pdf, name='reporte_proveedores_pdf'),
    path('proveedores/reporte/excel/', views.reporte_proveedores_excel, name='reporte_proveedores_excel'),
    path('reporte_presentaciones/', views.reporte_presentaciones_pdf, name='reporte_presentaciones'),
    path('presentaciones/reporte_excel/', views.reporte_presentaciones_excel, name='reporte_presentaciones_excel'),
    path('reporte_unidades_medida/', views.reporte_unidades_medida_pdf, name='reporte_unidades_medida'),
    path('unidades_medida/reporte/', views.reporte_unidades_medida_excel, name='reporte_unidades_medida_excel'),
    path('venta/reporte_pdf/', views.reporte_ventas_pdf, name='reporte_ventas_pdf'),
    path('reporte_ventas_excel/', views.reporte_ventas_excel, name='reporte_ventas_excel'),
    path('reporte_pdf/', views.reporte_productos_pdf, name='reporte_pdf'),
    path('reporte_excel/', views.reporte_productos_excel, name='reporte_excel'),

    ### Estados ###
    path('categorias/activar/<int:pk>/', views.activar_categoria, name='activar_categoria'),
    path('categorias/desactivar/<int:pk>/', views.desactivar_categoria, name='desactivar_categoria'),
    path('marcas/activar/<int:pk>/', views.activar_marca, name='activar_marca'),
    path('marcas/desactivar/<int:pk>/', views.desactivar_marca, name='desactivar_marca'),
    path('presentaciones/activar/<int:pk>/', views.activar_presentacion, name='activar_presentacion'),
    path('presentaciones/desactivar/<int:pk>/', views.desactivar_presentacion, name='desactivar_presentacion'),
    path('producto/activar/<int:pk>/', views.activar_producto, name='activar_producto'),
    path('producto/desactivar/<int:pk>/', views.desactivar_producto, name='desactivar_producto'),
    path('unidades_medida/activar/<int:pk>/', views.activar_unidades_medida, name='activar_unidades_medida'),
    path('unidades_medida/desactivar/<int:pk>/', views.desactivar_unidades_medida, name='desactivar_unidades_medida'),
    path('proveedores/activar/<int:pk>/', views.activar_proveedor, name='activar_proveedor'),
    path('proveedores/desactivar/<int:pk>/', views.desactivar_proveedor, name='desactivar_proveedor'),
    path('compra/activar/<int:pk>/', views.activar_compra, name='activar_compra'),
    path('compra/desactivar/<int:pk>/', views.desactivar_compra, name='desactivar_compra'),
    path('venta/activar/<int:pk>/', views.activar_venta, name='activar_venta'),
    path('venta/desactivar/<int:pk>/', views.desactivar_venta, name='desactivar_venta'),

    path('respaldos/', gestionar_respaldos, name='backup'),
    path('respaldos/crear/', CrearRespaldoView.as_view(), name='crear_respaldo'),
    path('respaldos/restaurar/', RestaurarRespaldoView.as_view(), name='restaurar_respaldo'),
    path('respaldos/descargar/<str:respaldo_id>/', descargar_respaldo, name='descargar_respaldo'),
    path('respaldos/eliminar/', EliminarRespaldoView.as_view(), name='eliminar_respaldo'),
    path('respaldos/filtrar/', filtrar_respaldos, name='filtrar_respaldos'),


    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='register/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='register/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='register/password_reset_complete.html'), name='password_reset_complete'),
        
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
