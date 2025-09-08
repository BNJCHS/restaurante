from django.urls import path
from . import views

urlpatterns = [
    path("crear/", views.crear_reserva, name="crear_reserva"),
    path("mis_reservas/", views.mis_reservas, name="mis_reservas"),
    path("confirmar/<int:pk>/", views.confirmar_reserva, name="confirmar_reserva"),
]