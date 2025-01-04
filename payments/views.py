from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PaymentMethod
from .forms import PaymentMethodForm


@login_required
def payment_methods(request):
    methods = PaymentMethod.objects.filter(user=request.user)
    return render(request, "payments/payment_methods.html", {"methods": methods})


@login_required
def add_payment_method(request):
    if request.method == "POST":
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            payment_method = form.save(commit=False)
            payment_method.user = request.user
            payment_method.save()
            return redirect("payment_methods")
    else:
        form = PaymentMethodForm()
    return render(request, "payments/add_payment_method.html", {"form": form})


@login_required
def edit_payment_method(request, method_id):
    payment_method = get_object_or_404(PaymentMethod, id=method_id, user=request.user)
    if request.method == "POST":
        form = PaymentMethodForm(request.POST, instance=payment_method)
        if form.is_valid():
            form.save()
            return redirect("payment_methods")
    else:
        form = PaymentMethodForm(instance=payment_method)
    return render(request, "payments/edit_payment_method.html", {"form": form})
