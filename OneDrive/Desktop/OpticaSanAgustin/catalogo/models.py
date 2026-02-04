from django.db import models

class Producto(models.Model):
    marca = models.CharField(max_length=100)      # Ej: Ray-Ban
    modelo = models.CharField(max_length=100)     # Ej: Aviator
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Ej: 450.00
    descripcion = models.TextField()              # Descripción larga
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True) # La foto
    
    # Datos técnicos (opcionales por ahora)
    material = models.CharField(max_length=50, default="Acetato")
    
    def __str__(self):
        return f"{self.marca} - {self.modelo}"