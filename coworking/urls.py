from django.urls import path
from .views import coworking_list, coworking_detail

urlpatterns = [
    path("", coworking_list, name="coworking_list"),
    path("space/<int:pk>/", coworking_detail, name="coworking_detail"),
]
