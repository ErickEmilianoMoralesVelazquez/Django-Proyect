from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/', lista_categorias, name='lista'),
    path('registrar/', agregar_categoria, name='registrar'),
    path('json/', vista_categorias, name='categorias'),
    path('post_get/', registro_combinado, name='post_get'),
    path('api/post/', post_categoria, name='post'),
]