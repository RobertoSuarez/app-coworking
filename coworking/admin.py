from django.contrib import admin
from .models import CoworkingSpace, SpaceImage


class SpaceImageInline(admin.TabularInline):
    model = SpaceImage
    extra = 1  # Número de formularios adicionales para subir imágenes


class CoworkingSpaceAdmin(admin.ModelAdmin):
    inlines = [SpaceImageInline]


admin.site.register(CoworkingSpace, CoworkingSpaceAdmin)
admin.site.register(SpaceImage)
