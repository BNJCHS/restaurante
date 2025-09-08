from django.urls import path
from . import views

urlpatterns = [
    # Panel Admin (AJAX dinámico)
    path('', views.dashboard, name='admin_dashboard'),
    # AJAX
    path('ajax/<str:section>/', views.ajax_section, name='ajax_section'),

    # Formularios
    path('platos/<int:pk>/editar/', views.editar_plato, name='plato_edit'),
    path('platos/<int:pk>/eliminar/', views.eliminar_plato, name='plato_eliminar'),

    path('pedidos/<int:pk>/editar/', views.pedido_edit, name='pedido_edit'),
    path('reservas/<int:pk>/editar/', views.reserva_edit, name='reserva_edit'),
]
