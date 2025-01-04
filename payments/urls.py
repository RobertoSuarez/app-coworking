from django.urls import path
from .views import (
    payment_methods,
    add_payment_method,
    edit_payment_method,
)

urlpatterns = [
    path("", payment_methods, name="payment_methods"),
    path("add/", add_payment_method, name="add_payment_method"),
    path("edit/<int:method_id>/", edit_payment_method, name="edit_payment_method"),
]
