from django.shortcuts import render
from django.views import generic
from .models import CoworkingSpace


class CoworkingListView(generic.ListView):
    model = CoworkingSpace
    template_name = "coworking/list_coworking.html"
    context_object_name = "coworkings"
