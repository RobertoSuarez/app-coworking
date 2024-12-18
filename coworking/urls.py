from django.urls import path
from .views import CoworkingListView

urlpatterns = [
    path("", CoworkingListView.as_view(), name="list_coworking"),
]
