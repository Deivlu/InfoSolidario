# articulos/apps.py
from django.apps import AppConfig # type: ignore

class ArticulosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # CORRECCIÓN: Debe coincidir con la carpeta y el settings.py
    name = 'apps.articulos' 
    verbose_name = 'Plataforma de Artículos Solidarios'