from django import forms
from .models import PaymentMethod


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = [
            "card_type",
            "card_number",
            "cardholder_name",
            "expiration_date",
            "cvv",
        ]
        widgets = {
            "expiration_date": forms.DateInput(attrs={"type": "date"}),
        }
