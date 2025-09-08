from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
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

@login_required
def editar_pedido_admin(request, pk):
    # Esta view la usaría un admin
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            pedido = form.save()
            if pedido.estado == "listo":
                # Enviar email al cliente
                asunto = f"Tu pedido está listo - Restaurante"
                mensaje = f"Hola {pedido.cliente.username},\n\nTu pedido de {pedido.plato} x{pedido.cantidad} está listo para entregar.\n\nGracias por elegirnos."
                send_mail(
                    asunto,
                    mensaje,
                    settings.DEFAULT_FROM_EMAIL,
                    [pedido.cliente.email],
                    fail_silently=False,
                )
            return redirect("lista_pedidos_admin")
    else:
        form = PedidoForm(instance=pedido)
    return render(request, "pedidos/editar_pedido_admin.html", {"form": form})
