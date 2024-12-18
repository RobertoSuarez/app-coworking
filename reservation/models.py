from django.db import models
from django.contrib.auth.models import User  # Importar el modelo de usuario predeterminado
from coworking.models import CoworkingSpace


# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    space = models.ForeignKey(CoworkingSpace, on_delete=models.CASCADE, related_name='reservations')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation by {self.user.username} for {self.space.name}"

        return self.nombre