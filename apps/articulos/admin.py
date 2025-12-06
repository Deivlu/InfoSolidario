from django.contrib import admin
from .models import Categoria, Articulo, Comentario

# Esto hace que aparezcan en el panel de administración de Django
admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(Comentario)