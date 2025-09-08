from django.urls import path
from . import views

urlpatterns = [
    path("crear/", views.crear_pedido, name="crear_pedido"),
    path("mis_pedidos/", views.mis_pedidos, name="mis_pedidos"),
    path("admin/editar/<int:pk>/", views.editar_pedido_admin, name="editar_pedido_admin"),
]