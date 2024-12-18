from django.db import models
from django.contrib.auth.models import User  # Importar el modelo de usuario predeterminado

class CoworkingSpace(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    services = models.JSONField(default=list, blank=True)  # Almacena listas de servicios
    type = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SpaceImage(models.Model):
    space = models.ForeignKey(CoworkingSpace, on_delete=models.CASCADE, related_name='images')
    image_url = models.TextField()

    def __str__(self):
        return f"Image for {self.space.name}"




