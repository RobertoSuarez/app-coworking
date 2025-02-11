from django.urls import path
from .views import (
    create_reservation,
    my_reservations,
    cancel_reservation,
    all_reservations,
    get_reservations,
    accept_contract,
)

urlpatterns = [
    path("create/<int:space_id>/", create_reservation, name="create_reservation"),
    path("my_reservations/", my_reservations, name="my_reservations"),
    path("cancel/<int:reservation_id>/", cancel_reservation, name="cancel_reservation"),
    path("all_reservations/", all_reservations, name="all_reservations"),
    path("api/reservations/<int:space_id>/", get_reservations, name="get_reservations"),
    path(
        "reservation/accept/<int:reservation_id>/",
        accept_contract,
        name="accept_contract",
    ),
]
