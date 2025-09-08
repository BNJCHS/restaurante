from django import forms
from .models import Plato
from pedidos.models import Pedido
from reservas.models import Reserva

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ["nombre", "descripcion", "precio", "disponible"]

class PedidoAdminForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["cliente", "plato", "cantidad", "direccion", "estado"]

class ReservaAdminForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["nombre", "email", "telefono", "fecha", "hora", "cantidad_personas", "mensaje"]

