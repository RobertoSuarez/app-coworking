from django.urls import path
from .views import coworking_list, coworking_details

urlpatterns = [
    path("", coworking_list, name="coworking_list"),
    path("space/<int:pk>/", coworking_details, name="coworking_detail"),
]
