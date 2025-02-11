from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core import serializers
from decimal import Decimal
from coworking.models import CoworkingSpace
from users.models import UserProfile
from .models import Reservation
from .forms import ReservationForm
from .utils import send_whatsapp_message, send_whatsapp_message_via_api
from django.http import JsonResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages


@login_required
def create_reservation(request, space_id):
    userProfile = UserProfile.objects.get(user=request.user)
    space = get_object_or_404(CoworkingSpace, id=space_id)
    if request.method == "POST":
        form = ReservationForm(request.POST, user=request.user)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.space = space  # Asegurarse de asignar el espacio

            # Calcular el precio total basado en el tipo de reserva
            duration = (reservation.end_time - reservation.start_time).total_seconds()
            if reservation.reservation_type == "hour":
                hours = Decimal(duration / 3600)
                reservation.total_price = space.price_per_hour * hours
            elif reservation.reservation_type == "day":
                days = Decimal(duration / 86400)
                reservation.total_price = space.price_per_day * days
            elif reservation.reservation_type == "week":
                weeks = Decimal(duration / 604800)
                reservation.total_price = space.price_per_week * weeks
            elif reservation.reservation_type == "month":
                months = Decimal(duration / 2592000)
                reservation.total_price = space.price_per_month * months

            reservation.save()

            # Preparar el correo electrónico con el contrato
            subject = f"Contrato de Alquiler para {space.name}"
            from_email = settings.DEFAULT_FROM_EMAIL
            to = [request.user.email]

            print(
                "Nombre del usuario:",
                request.user.get_full_name() or request.user.username,
            )
            print("Correo del usuario:", request.user.email)

            # Generar la URL para aceptar el contrato (se debe definir la vista 'accept_contract')
            accept_contract_url = request.build_absolute_uri(
                reverse("accept_contract", args=[reservation.id])
            )

            # Renderizar el template HTML del contrato
            html_content = render_to_string(
                "reservation/contract_email.html",
                {
                    "reservation": reservation,
                    "space": space,
                    "user": request.user,
                    "accept_contract_url": accept_contract_url,
                },
            )
            text_content = "Por favor, revise el contrato adjunto en el correo HTML."

            # Enviar el email
            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # Opcional: enviar mensaje de WhatsApp (comentado)
            # message = (
            #     f"Hola {request.user.username}, tu reserva para '{space.name}' ha sido confirmada 🎉. \n"
            #     f"Detalles de la reserva: \nInicio - {reservation.start_time.strftime('%d/%m/%Y %H:%M')} ⏰, \n"
            #     f"Fin - {reservation.end_time.strftime('%d/%m/%Y %H:%M')} ⏰. \n"
            #     f"Dirección: {space.location}."
            # )
            # send_whatsapp_message(userProfile.phone_number, message)
            # send_whatsapp_message_via_api(userProfile.phone_number, message)

            return redirect("coworking_detail", pk=space.id)
    else:
        form = ReservationForm(user=request.user)
    return render(
        request, "reservation/create_reservation.html", {"form": form, "space": space}
    )


@login_required
def my_reservations(request):
    now = timezone.now().astimezone(timezone.get_current_timezone())
    reservations = Reservation.objects.filter(user=request.user).order_by("-created_at")
    context = {"reservations": reservations, "now": now}
    return render(request, "reservation/my_reservations.html", context)


@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if reservation.start_time > timezone.now():
        reservation.delete()
    return redirect("my_reservations")


@login_required
def all_reservations(request):
    coworking_space_id = request.GET.get("coworking_space")
    if coworking_space_id:
        reservations = Reservation.objects.filter(space_id=coworking_space_id).order_by(
            "-created_at"
        )
    else:
        reservations = Reservation.objects.all().order_by("-created_at")

    now = timezone.now().astimezone(timezone.get_current_timezone())
    coworking_spaces = CoworkingSpace.objects.all()

    context = {
        "reservations": reservations,
        "coworking_spaces": coworking_spaces,
        "now": now,
    }
    return render(request, "reservation/all_reservation_admin.html", context)


def get_reservations(request, space_id):
    reservations = Reservation.objects.filter(space_id=space_id)
    events = []
    for reservation in reservations:
        events.append(
            {
                "title": "Reservado",
                "start": reservation.start_time.isoformat(),
                "end": reservation.end_time.isoformat(),
                "color": "#ff6961",  # pastel red
            }
        )
    return JsonResponse(events, safe=False)


def all_reservations_admin(request):
    coworking_space_id = request.GET.get("coworking_space")
    if coworking_space_id:
        reservations = Reservation.objects.filter(space_id=coworking_space_id).order_by(
            "-created_at"
        )
    else:
        reservations = Reservation.objects.all().order_by("-created_at")

    coworking_spaces = CoworkingSpace.objects.all()

    context = {
        "reservations": reservations,
        "coworking_spaces": coworking_spaces,
    }
    return render(request, "reservation/all_reservation_admin.html", context)


@login_required
def accept_contract(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    # Aquí podrías marcar en el modelo Reservation que el contrato ha sido aceptado,
    # por ejemplo: reservation.contract_accepted = True
    # reservation.save()

    messages.success(request, "Ha aceptado el contrato. Su reserva está confirmada.")
    return redirect("coworking_detail", pk=reservation.space.id)
