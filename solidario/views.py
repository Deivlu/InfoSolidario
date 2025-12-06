from django.shortcuts import render
# 1. Importar el modelo Articulo para poder pedirle datos
from apps.articulos.models import Articulo

def Home(request):
    # 2. Pedimos los últimos 4 artículos (ordenados por fecha descendente)
    # [:4] significa "dame solo los primeros 4"
    ultimos_articulos = Articulo.objects.order_by('-fecha_publicacion')[:4]
    
    # 3. Guardamos en un diccionario de contexto
    contexto = {
        'articulos_destacados': ultimos_articulos
    }
    
    # 4. Se lo enviamos al template
    return render(request, 'home.html', contexto)

def Contacto(request):
    return render(request, 'contacto.html')