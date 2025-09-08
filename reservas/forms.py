from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["nombre", "email", "telefono", "fecha", "hora", "cantidad_personas", "mensaje"]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "hora": forms.TimeInput(attrs={"type": "time"}),
            "mensaje": forms.Textarea(attrs={"rows": 3}),
        }
