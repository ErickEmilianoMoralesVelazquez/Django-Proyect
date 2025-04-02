from django.shortcuts import render, redirect
from .models import Categoria
from django.http import JsonResponse
from .forms import categoriaForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Categoria

def lista_categorias(request):
    categorias = Categoria.objects.all()

    data=[
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categorias
    ]

    return JsonResponse(data, safe=False)

def agregar_categoria(request):
    if request.method == 'POST':
        form=categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    else:
        form = categoriaForm()
    return render(request, 'regCategoria.html', {'form': form})
# Create your views here.

def vista_categorias(request):
    return render(request, 'categorias.html')

def registro_combinado(request):
    return render(request, 'combinado.html')

@csrf_exempt
def post_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        imagen = request.POST.get('imagen')
        categoria = Categoria(nombre=nombre, imagen=imagen)
        categoria.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

