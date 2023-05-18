from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from .models import CarritoDeCompras, Producto
from django.views import View

class CarritoView(View):      
    def agregar_producto_carrito(request):
        # Verifica si la solicitud es de tipo 'POST'
        if request.method == 'POST':
            # Obtener el id del producto y la cantidad deseada a partir de la solicitud 
            id_producto = request.POST.get('id_producto')
            cantidad = request.POST.get('cantidad')
            if not id_producto or not cantidad:
                # Si falta algún parámetro, retornar error 400 con arreglo de errores
                errores = {'error': ['Falta el id del producto o la cantidad.']}
                return HttpResponseBadRequest(JsonResponse(errores, status=400))

            try:
                # Buscar el producto en la base de datos
                producto = Producto.objects.get(id=id_producto)
                # Agregar el producto al carrito con la cantidad deseada
                carrito = CarritoDeCompras.agregar_producto(request.user, producto, cantidad)
                # Retornar una respuesta 201 con los atributos del producto y la cantidad
                respuesta = {'producto': carrito.producto.to_dict(), 'cantidad': carrito.cantidad}
                return JsonResponse(respuesta, status=201)
            except Producto.DoesNotExist:
                # Si el producto no existe, retornar error 400 con arreglo de errores
                errores = {'error': ['El producto con id {} no existe.'.format(id_producto)]}
                return HttpResponseBadRequest(JsonResponse(errores, status=400))
            except Exception as e:
                # Si ocurre un error en el servidor, retornar error 500 con mensaje de error
                mensaje_error = 'Ocurrió un error en el servidor: {}'.format(str(e))
                return HttpResponseServerError(JsonResponse({'error': mensaje_error}, status=500))
        else:
            # Si la solicitud no es POST, retornar error 503 (Service Unavailable)
            return JsonResponse({'errors': {'general': 'Este servicio no está permitido.'}}, status=503)
