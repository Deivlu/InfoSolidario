from django.contrib import admin
from .models import PerfilUsuario

# Esto permite ver quién es colaborador y quién no
admin.site.register(PerfilUsuario)