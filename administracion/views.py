from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Plato
from pedidos.models import Pedido
from reservas.models import Reserva
from .forms import PlatoForm, PedidoAdminForm, ReservaAdminForm

# ---------------- AJAX Sections ----------------
def ajax_section(request, section):
    if section == "dashboard":
        total_reservas = Reserva.objects.count()
        total_pedidos = Pedido.objects.count()
        total_platos = Plato.objects.count()
        return render(request, "administracion/ajax/dashboard.html", {
            "total_reservas": total_reservas,
            "total_pedidos": total_pedidos,
            "total_platos": total_platos
        })
    elif section == "platos":
        platos = Plato.objects.all()
        return render(request, "administracion/ajax/platos_list.html", {"platos": platos})
    elif section == "pedidos":
        pedidos = Pedido.objects.all()
        return render(request, "administracion/ajax/pedidos_list.html", {"pedidos": pedidos})
    elif section == "reservas":
        reservas = Reserva.objects.all()
        return render(request, "administracion/ajax/reservas_list.html", {"reservas": reservas})
    return render(request, "administracion/ajax/404.html")

def dashboard(request):
    total_pedidos = Pedido.objects.count()
    pedidos_pendientes = Pedido.objects.filter(estado="pendiente").count()
    total_reservas = Reserva.objects.count()
    reservas_proximas = Reserva.objects.filter(fecha__gte=timezone.now().date()).count()
    total_platos = Plato.objects.count()

    context = {
        'total_pedidos': total_pedidos,
        'pedidos_pendientes': pedidos_pendientes,
        'total_reservas': total_reservas,
        'reservas_proximas': reservas_proximas,
        'total_platos': total_platos
    }
    return render(request, 'administracion/ajax/dashboard.html', context)


# ---------------- CRUD PLATOS ----------------
def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, "administracion/ajax/platos_list.html", {"platos": platos})

def crear_plato(request):
    if request.method == "POST":
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("plato_list")
    else:
        form = PlatoForm()
    return render(request, "administracion/ajax/platos_form.html", {"form": form})

def editar_plato(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == "POST":
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect("plato_list")
    else:
        form = PlatoForm(instance=plato)
    return render(request, "administracion/ajax/platos_form.html", {"form": form})

def eliminar_plato(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == "POST":
        plato.delete()
        return redirect("plato_list")
    return render(request, "administracion/ajax/platos_delete.html", {"plato": plato})


# ---------------- PEDIDOS ----------------
def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'administracion/ajax/pedidos_list.html', {'pedidos': pedidos})

def pedido_edit(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoAdminForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedido_list')
    else:
        form = PedidoAdminForm(instance=pedido)
    return render(request, 'administracion/ajax/pedido_form.html', {'form': form})


# ---------------- RESERVAS ----------------
def reserva_list(request):
    reservas = Reserva.objects.all()
    return render(request, 'administracion/ajax/reservas_list.html', {'reservas': reservas})

def reserva_edit(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaAdminForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_list')
    else:
        form = ReservaAdminForm(instance=reserva)
    return render(request, 'administracion/ajax/reserva_form.html', {'form': form})
