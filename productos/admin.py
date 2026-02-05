from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, SubCategoria, Marca, Producto, Pedido

# --- PERSONALIZACIÓN DEL ENCABEZADO ---
admin.site.site_header = "Mundo Limpieza - 526" # Título de la pestaña y barra superior
admin.site.index_title = "Panel de Control de Stock y Pedidos"
admin.site.site_url = '/catalogo/' # ESTO HACE QUE EL BOTÓN "VER SITIO" VAYA AL CATÁLOGO
# --------------------------------------

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('ver_imagen', 'nombre', 'medida_completa', 'marca', 'precio', 'stock', 'oferta', 'disponible')
    list_editable = ('precio', 'stock', 'oferta', 'disponible')
    list_filter = ('disponible', 'oferta', 'marca', 'subcategoria')
    search_fields = ('nombre', 'marca__nombre')
    
    def ver_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 5px; object-fit: cover;" />', obj.imagen.url)
        return "Sin foto"
    ver_imagen.short_description = 'Foto'

    def medida_completa(self, obj):
        return f"{obj.medida_valor} {obj.unidad}"
    medida_completa.short_description = 'Medida'

@admin.action(description='DESCONTAR STOCK: Marcar como entregado')
def procesar_entrega(modeladmin, request, queryset):
    for pedido in queryset:
        if not pedido.entregado:
            for item in pedido.productos_data:
                prod = Producto.objects.filter(nombre=item['nombre']).first()
                if prod:
                    prod.stock -= int(item['cantidad'])
                    prod.save()
            pedido.entregado = True
            pedido.save()

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'total', 'entregado')
    list_filter = ('entregado', 'fecha')
    actions = [procesar_entrega]

# También registramos los otros modelos para poder cargar marcas y categorías
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Marca)