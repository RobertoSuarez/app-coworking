from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Configuramos las rutas y los archivos estaticos.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("coworking/", include("coworking.urls")),
    path("users/", include("users.urls")),
    path("", include("landingPages.urls")),
    path("reservation/", include("reservation.urls")),
    path("payments/", include("payments.urls")),
    path("assistant/", include("assistant.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
