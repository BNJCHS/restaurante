from django.db import models
from django.conf import settings

class Pedido(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("preparando", "Preparando"),
        ("listo", "Listo para entregar"),
        ("entregado", "Entregado"),
    ]

    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plato = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=1)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.cliente.username} - {self.plato} x{self.cantidad}"
