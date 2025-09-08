from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReservaForm
from .models import Reserva

@login_required
def crear_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.cliente = request.user
            reserva.save()
            
            # Enviar email de confirmación
            asunto = f"Confirma tu reserva - Restaurante"
            link_confirmacion = request.build_absolute_uri(
                f"/reservas/confirmar/{reserva.id}/"
            )
            mensaje = f"Hola {reserva.nombre},\n\nTu reserva para el {reserva.fecha} a las {reserva.hora} está pendiente de confirmación.\n\nConfirma tu reserva haciendo clic aquí: {link_confirmacion}\n\nGracias por elegirnos."
            send_mail(
                asunto,
                mensaje,
                settings.DEFAULT_FROM_EMAIL,
                [reserva.email],
                fail_silently=False,
            )
            return redirect("mis_reservas")
    else:
        form = ReservaForm()
    return render(request, "reservas/crear_reserva.html", {"form": form})

@login_required
def confirmar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    reserva.confirmado = True
    reserva.save()
    return render(request, "reservas/reserva_confirmada.html", {"reserva": reserva})

@login_required
def mis_reservas(request):
    reservas = Reserva.objects.filter(cliente=request.user).order_by("-fecha", "-hora")
    return render(request, "reservas/mis_reservas.html", {"reservas": reservas})
