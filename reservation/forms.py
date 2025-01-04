from django import forms
from .models import Reservation, PaymentMethod


class ReservationForm(forms.ModelForm):
    payment_card = forms.ModelChoiceField(
        queryset=PaymentMethod.objects.none(),
        required=False,
        empty_label="Seleccione una tarjeta registrada",
        widget=forms.Select(
            attrs={
                "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            }
        ),
    )

    class Meta:
        model = Reservation
        fields = [
            "reservation_type",
            "start_time",
            "end_time",
            "payment_method",
            "payment_card",
        ]
        labels = {
            "reservation_type": "Tipo de Reserva",
            "start_time": "Hora de Inicio",
            "end_time": "Hora de Finalización",
        }
        widgets = {
            "reservation_type": forms.Select(
                attrs={
                    "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                }
            ),
            "start_time": forms.DateTimeInput(
                attrs={
                    "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                    "type": "datetime-local",
                }
            ),
            "end_time": forms.DateTimeInput(
                attrs={
                    "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                    "type": "datetime-local",
                }
            ),
            "payment_method": forms.Select(
                attrs={
                    "class": "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["payment_card"].queryset = PaymentMethod.objects.filter(
                user=user
            )
