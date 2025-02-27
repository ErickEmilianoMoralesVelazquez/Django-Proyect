from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets # Vamos a crear una vista de varias
from rest_framework.renderers import JSONRenderer

class ProductoViewSet(viewsets.ModelViewSet):
    # Tres variables clave 
    # 1. queryset permitir saber a que objeto hacer referencia
    queryset = Producto.objects.all()
    # 2. Serializar los objetos
    serializer_class = ProductoSerializer
    # 3. Renderizar las respuestas
    renderer_classes = [JSONRenderer]
    # 4. Establecer que métodos puede usar
    # http_method_names = ['get', 'post', 'put', 'delete']