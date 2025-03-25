from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, profile, terms_and_conditions, send_otp, verify_otp

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", profile, name="profile"),
    path("terms-and-conditions/", terms_and_conditions, name="terms_and_conditions"),
    path("send-otp/", send_otp, name="send_otp"),
    path("verify-otp/", verify_otp, name="verify_otp"),
    # Otras rutas...
]
