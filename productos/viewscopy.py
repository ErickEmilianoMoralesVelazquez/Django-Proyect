from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto
from .forms import productoForm
import json

#Metodo que devuelve el JSON
def lista_productos(request):
    productos = Producto.objects.all()

    data=[
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]

    return JsonResponse(data, safe=False)


# def agregar_producto(request):
#     if request.method == 'POST':
#         form=productoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lista')
#     else:
#         form = productoForm()
#     return render(request, 'agregar.html', {'form': form})

def agregar_producto(request):
    form = productoForm()
    return render(request, 'agregar.html', {'form': form})

# Create your views here.

#Funcion que registre sin recargar la pagina
def registrar_producto(request):
    #Checar si se maneja POST
    if request.method == 'POST':
        try:
            #Intentar optener los datos del body
            data = json.loads(request.body) #Hace que el parametro se vuelva json
            producto = Producto.objects.create(
                #Es un constructor
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen']
            )
            return JsonResponse({'mensaje': 'Registro exitoso', 'id':producto.id},status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Metodo no soportado'}, status=405)

def eliminar_producto(request, id):
    try:
        producto = Producto.objects.get(id=id)
        producto.delete()
        return JsonResponse({'mensaje': 'Producto eliminado'}, status=200)
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'El producto no existe'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
def modificar_producto(request, id):
    try:
        producto = Producto.objects.get(id=id)
        data = json.loads(request.body)
        producto.nombre = data['nombre']
        producto.precio = data['precio']
        producto.imagen = data['imagen']
        producto.save()
        return JsonResponse({'mensaje': 'Producto modificado'}, status=200)
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'El producto no existe'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
def obtener_producto(request, id):
    try:
        producto = Producto.objects.get(id=id)
        data = {
            'nombre': producto.nombre,
            'precio': producto.precio,
            'imagen': producto.imagen
        }
        return JsonResponse(data, status=200)
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'El producto no existe'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400
    )

