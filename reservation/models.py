from django.db import models
from django.contrib.auth.models import (
    User,
)  # Importar el modelo de usuario predeterminado
from coworking.models import CoworkingSpace
from payments.models import PaymentMethod


# Create your models here.
class Reservation(models.Model):
    RESERVATION_TYPE_CHOICES = [
        ("hour", "Por hora"),
        ("day", "Por día"),
        ("week", "Por semana"),
        ("month", "Por mes"),
    ]

    PAYMENT_METHOD_CHOICES = [
        ("credit_card", "Tarjeta de Crédito/Débito"),
        ("cash", "Efectivo"),
        ("bank_transfer", "Transferencia Bancaria"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reservations"
    )
    space = models.ForeignKey(
        CoworkingSpace, on_delete=models.CASCADE, related_name="reservations"
    )
    reservation_type = models.CharField(
        max_length=10, choices=RESERVATION_TYPE_CHOICES, default="hour"
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD_CHOICES, default="cash"
    )
    payment_card = models.ForeignKey(
        PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation by {self.user.username} for {self.space.name}"
