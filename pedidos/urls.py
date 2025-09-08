from django.urls import path
from . import views

urlpatterns = [
    path("nuevo/", views.crear_pedido, name="crear_pedido"),
    path("mis-pedidos/", views.mis_pedidos, name="mis_pedidos"),
]
