from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/', lista_productos, name='lista'),
    path('agregar/', agregar_producto, name='agregar'),
    path('api/post/', registrar_producto, name='post')
]