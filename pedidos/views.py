from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PedidoForm
from .models import Pedido

@login_required
def crear_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.cliente = request.user
            pedido.save()
            return redirect("mis_pedidos")
    else:
        form = PedidoForm()
    return render(request, "pedidos/crear_pedido.html", {"form": form})

@login_required
def mis_pedidos(request):
    pedidos = Pedido.objects.filter(cliente=request.user).order_by("-fecha")
    return render(request, "pedidos/mis_pedidos.html", {"pedidos": pedidos})
