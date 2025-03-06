from django.shortcuts import render
from rest_framework import viewsets
from .models import Alumno
from .serializers import AlumnoSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    renderer_classes = [JSONRenderer]
    # http_method_names = ['get', 'post', 'put', 'delete']

def index(request):
    return render(request, './morales_erick.html')