from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class PaymentMethod(models.Model):
    CARD_TYPE_CHOICES = [
        ("visa", "Visa"),
        ("mastercard", "MasterCard"),
        ("amex", "American Express"),
        ("discover", "Discover"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payment_methods"
    )
    card_type = models.CharField(max_length=20, choices=CARD_TYPE_CHOICES)
    card_number = models.CharField(max_length=16)
    cardholder_name = models.CharField(max_length=100)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.card_number.isdigit():
            raise ValidationError(
                "El número de la tarjeta solo puede contener dígitos."
            )

    def __str__(self):
        return f"{self.card_type} - {self.card_number[-4:]}"

    class Meta:
        verbose_name = "Método de Pago"
        verbose_name_plural = "Métodos de Pago"
