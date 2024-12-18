from django.db import models
from django.contrib.auth.models import User  # Importar el modelo de usuario predeterminado
from coworking.models import CoworkingSpace


# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    space = models.ForeignKey(CoworkingSpace, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.space.name}"