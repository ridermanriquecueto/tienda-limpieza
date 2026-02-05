from django.shortcuts import render
from .models import Producto, Categoria
from .models import Pedido
from django.http import JsonResponse
import json
# Datos comunes para la tienda (Centralizado para no repetir)
INFO_TIENDA = {
    'nombre_tienda': 'Limpieza 526',
    'direccion': 'Calle 526 número 3777',
    'whatsapp': '5492216769436' # Formato internacional listo para el link
}

def inicio(request):
    return render(request, 'productos/inicio.html', INFO_TIENDA)

def catalogo(request):
    categoria_id = request.GET.get('categoria')
    solo_ofertas = request.GET.get('oferta')
    
    # Empezamos filtrando solo lo que marcaste como "disponible" en el Admin
    productos = Producto.objects.filter(disponible=True)
    
    # Si el usuario eligió una categoría en los botones
    if categoria_id:
        productos = productos.filter(subcategoria__categoria_id=categoria_id)
    
    # Si el usuario quiere ver solo las ofertas
    if solo_ofertas == 'true':
        productos = productos.filter(oferta=True)
        
    categorias = Categoria.objects.all()
    
    context = {
        **INFO_TIENDA, 
        'productos': productos, 
        'categorias': categorias,
        'filtro_oferta': solo_ofertas == 'true' # Para saber si estamos viendo ofertas
    }
    return render(request, 'productos/catalogo.html', context)

def pedido(request):
    # Pasamos INFO_TIENDA para que el botón de WhatsApp tenga el número
    return render(request, 'productos/pedido.html', INFO_TIENDA)

def contacto(request):
    return render(request, 'productos/contacto.html', INFO_TIENDA)

def guardar_pedido(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nuevo_pedido = Pedido.objects.create(
            cliente=data['nombre'],
            detalle_envio=data['detalle'],
            productos_data=data['carrito'],
            total=data['total']
        )
        return JsonResponse({'status': 'ok', 'pedido_id': nuevo_pedido.id})
