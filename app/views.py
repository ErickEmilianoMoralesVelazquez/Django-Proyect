from django.http import HttpResponse
from django.shortcuts import render
from app.utils import google_search

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def error_404_view(request, exception):
    render(request, '404.html', status=404)

def error_500_view(request, exception):
    render(request, '500.html', status=500)

def error(request, exception):
    return 7 / 0

def onepage(request):
    return render(request, 'onepage.html', status=200)

def prueba(request):
    nombre = request.GET.get('nombre', '')
    edad = request.GET.get('edad', '')
    
    persona = {
        'nombres': nombre,
        'edad': edad,
        'descripcion': nombre + ' tiene ' + edad + ' años'
    }

    persona2 = {
        'nombres': 'Emiliano',
        'edad': '28',
        'descripcion': nombre + ' tiene ' + edad + ' años'
    }

    persona3 = {
        'nombres': 'ERICK EMILIANO',
        'edad': '20',
        'descripcion': nombre + ' tiene ' + edad + ' años'
    }

    conjunto = [persona, persona2, persona3]

    if(persona['nombres'] == 'Erick'):
        persona['descripcion'] = 'Erick es el mejor'

    print(persona['nombres'])

    return render(
        request, 
        'prueba.html', 
        {'objeto': persona, 'saludo': 'Hola Mundo', 'personas': conjunto}
        )

def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})

from django.http import JsonResponse
from django.shortcuts import render
from .models import ErrorLog

def error_logs(request):
    return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})