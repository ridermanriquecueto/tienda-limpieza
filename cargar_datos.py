import os
import django

# 1. Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda_limpieza.settings') 
django.setup()

from productos.models import Producto, Categoria, SubCategoria, Marca

def cargar():
    print("--- Iniciando carga de datos ---")

    # 2. Creamos una Categoría, Subcategoría y Marca por defecto
    cat, _ = Categoria.objects.get_or_create(nombre="Limpieza")
    sub, _ = SubCategoria.objects.get_or_create(categoria=cat, nombre="General")
    marca_generica, _ = Marca.objects.get_or_create(nombre="Varios")

    # Lista de 15 productos reales (Nombre, Precio, Valor Medida, Unidad)
    productos_nuevos = [
        ["Jabón Líquido Ariel", 8500.00, 3.0, 'L'],
        ["Detergente Magistral", 2100.00, 500.0, 'UN'],
        ["Desengrasante Mr Músculo", 3200.00, 500.0, 'UN'],
        ["Suavizante Vivere", 4500.00, 3.0, 'L'],
        ["Limpiador Poett", 1800.00, 900.0, 'UN'],
        ["Lavandina Ayudín", 1500.00, 1.0, 'L'],
        ["Limpiavidrios Cif", 2800.00, 500.0, 'UN'],
        ["Papel Higiénico Higienol", 3500.00, 4.0, 'UN'],
        ["Rollos Sussex Gigante", 2900.00, 3.0, 'UN'],
        ["Pastilla Inodoro Harpic", 1200.00, 1.0, 'UN'],
        ["Esponja Mortimer", 800.00, 1.0, 'UN'],
        ["Bolsas Residuos 45x60", 1100.00, 10.0, 'UN'],
        ["Aerosol Glade", 2400.00, 360.0, 'UN'],
        ["Blem Lustramuebles", 3600.00, 360.0, 'UN'],
        ["Guantes Mapa", 2200.00, 1.0, 'UN']
    ]

    for p in productos_nuevos:
        # Usamos subcategoria, medida_valor y unidad que son tus campos reales
        obj, creado = Producto.objects.get_or_create(
            nombre=p[0],
            defaults={
                'subcategoria': sub,
                'marca': marca_generica,
                'precio': p[1],
                'medida_valor': p[2],
                'unidad': p[3],
                'stock': 20,
                'disponible': True,
                'oferta': False
            }
        )
        if creado:
            print(f"✅ Añadido: {p[0]}")
        else:
            print(f"🟡 Ya existía: {p[0]}")

    print("--- Carga finalizada con éxito ---")

if __name__ == '__main__':
    cargar()