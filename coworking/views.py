from django.shortcuts import render, get_object_or_404
from .models import CoworkingSpace
from django.db.models import Q


def coworking_list(request):
    query = request.GET.get("search")
    if query:
        spaces = CoworkingSpace.objects.prefetch_related("images").filter(
            Q(name__icontains=query)
            | Q(description__icontains=query)
            | Q(location__icontains=query)
        )
    else:
        spaces = CoworkingSpace.objects.prefetch_related("images").all()

    return render(request, "coworking/coworking_list.html", {"spaces": spaces})


def coworking_detail(request, pk):
    space = get_object_or_404(CoworkingSpace, pk=pk)
    return render(request, "coworking/coworking_detail.html", {"space": space})
