from django.contrib import admin
from .models import Producto

# Esto hace que aparezca en el panel
admin.site.register(Producto)