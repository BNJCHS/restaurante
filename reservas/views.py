from django.shortcuts import render, redirect
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
            return redirect("mis_reservas")
    else:
        form = ReservaForm()
    return render(request, "reservas/crear_reserva.html", {"form": form})

@login_required
def mis_reservas(request):
    reservas = Reserva.objects.filter(cliente=request.user).order_by("-fecha", "-hora")
    return render(request, "reservas/mis_reservas.html", {"reservas": reservas})
