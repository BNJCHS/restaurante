from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    # Platos
    path("platos/", views.lista_platos, name="lista_platos"),
    path("platos/nuevo/", views.crear_plato, name="crear_plato"),
    path("platos/<int:pk>/editar/", views.editar_plato, name="editar_plato"),
    path("platos/<int:pk>/eliminar/", views.eliminar_plato, name="eliminar_plato"),

    # Pedidos
    path("pedidos/", views.lista_pedidos, name="lista_pedidos"),
    path("pedidos/<int:pk>/editar/", views.editar_pedido, name="editar_pedido"),

    # Reservas
    path("reservas/", views.lista_reservas, name="lista_reservas"),
    path("reservas/<int:pk>/editar/", views.editar_reserva, name="editar_reserva"),
]
