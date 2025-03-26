from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from .forms import UserProfileForm
from .models import UserProfile
import pyotp


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")


@login_required
def profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserProfileForm(instance=profile)
    return render(request, "users/profile.html", {"form": form})


def terms_and_conditions(request):
    return render(request, "users/terms_and_conditions.html")


def send_otp(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            user_profile, created = UserProfile.objects.get_or_create(user=user)

            if not user_profile.otp_secret:
                user_profile.otp_secret = pyotp.random_base32()
                user_profile.save()
            # Crear el objeto TOTP con un intervalo de 300 segundos (5 minutos)
            totp = pyotp.TOTP(user_profile.otp_secret, interval=300)
            otp = totp.now()
            print("opt: ", otp)

            from_email = settings.DEFAULT_FROM_EMAIL
            # Enviar OTP por correo electrónico
            send_mail(
                "Tu código OTP",
                f"Tu código OTP es: {otp}",
                from_email,
                [user.email],
            )
            request.session["otp_user_id"] = user.id
            return redirect("verify_otp")
        else:
            return render(
                request, "users/login.html", {"error": "Credenciales inválidas"}
            )
    return render(request, "users/login.html")


def verify_otp(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        print(otp)
        user_id = request.session.get("otp_user_id")
        print("user_id", user_id)
        if not user_id:
            return redirect("login")
        user = User.objects.get(id=user_id)
        user_profile = UserProfile.objects.get(user=user)
        print("user secret: ", user_profile.otp_secret)
        # Crear el objeto TOTP con un intervalo de 300 segundos (5 minutos)
        totp = pyotp.TOTP(user_profile.otp_secret, interval=300)
        result = totp.verify(otp)
        print("result: ", result)

        if result:
            login(request, user)
            return redirect("profile")
        else:
            return render(request, "users/verify_otp.html", {"error": "OTP inválido"})
    return render(request, "users/verify_otp.html")
