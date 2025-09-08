from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Plato
from pedidos.models import Pedido
from reservas.models import Reserva
from .forms import PlatoForm, PedidoAdminForm, ReservaAdminForm


# ---------------- DASHBOARD ----------------
def dashboard(request):
    total_pedidos = Pedido.objects.count()
    pedidos_pendientes = Pedido.objects.filter(estado="pendiente").count()
    total_reservas = Reserva.objects.count()
    reservas_proximas = Reserva.objects.filter(fecha__gte=timezone.now().date()).count()
    total_platos = Plato.objects.count()

    context = {
        "total_pedidos": total_pedidos,
        "pedidos_pendientes": pedidos_pendientes,
        "total_reservas": total_reservas,
        "reservas_proximas": reservas_proximas,
        "total_platos": total_platos,
    }
    return render(request, "administracion/dashboard.html", context)


# ---------------- CRUD PLATOS ----------------
def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, "administracion/platos_list.html", {"platos": platos})

def crear_plato(request):
    if request.method == "POST":
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_platos")
    else:
        form = PlatoForm()
    return render(request, "administracion/plato_form.html", {"form": form})

def editar_plato(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == "POST":
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect("lista_platos")
    else:
        form = PlatoForm(instance=plato)
    return render(request, "administracion/plato_form.html", {"form": form})

def eliminar_plato(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == "POST":
        plato.delete()
        return redirect("lista_platos")
    return render(request, "administracion/plato_delete.html", {"plato": plato})


# ---------------- CRUD PEDIDOS ----------------
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, "administracion/pedidos_list.html", {"pedidos": pedidos})

def editar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoAdminForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect("lista_pedidos")
    else:
        form = PedidoAdminForm(instance=pedido)
    return render(request, "administracion/pedido_form.html", {"form": form})


# ---------------- CRUD RESERVAS ----------------
def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, "administracion/reservas_list.html", {"reservas": reservas})

def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        form = ReservaAdminForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect("lista_reservas")
    else:
        form = ReservaAdminForm(instance=reserva)
    return render(request, "administracion/reserva_form.html", {"form": form})
