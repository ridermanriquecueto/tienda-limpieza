from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='subcategorias')
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.categoria.nombre} - {self.nombre}"

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    UNIDADES_CHOICES = [
        ('L', 'Litros'),
        ('KG', 'Kilogramos'),
        ('UN', 'Unidades'),
    ]
    
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    
    unidad = models.CharField(max_length=2, choices=UNIDADES_CHOICES, default='UN')
    medida_valor = models.DecimalField(max_digits=5, decimal_places=2, help_text="Ej: 1.5, 5, 500")
    
    oferta = models.BooleanField(default=False, verbose_name="¿Está en Oferta?")
    precio_oferta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    disponible = models.BooleanField(default=True, verbose_name="¿Mostrar en Web?")

    def __str__(self):
        return f"{self.nombre} ({self.medida_valor}{self.unidad}) - {self.marca}"



class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    detalle_envio = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    # Guardaremos la lista de productos como texto para procesarla luego
    productos_data = models.JSONField() 
    total = models.DecimalField(max_digits=10, decimal_places=2)
    entregado = models.BooleanField(default=False, verbose_name="¿Ya se entregó y cobró?")

    def __str__(self):
        estado = "✅ ENTREGADO" if self.entregado else "⏳ PENDIENTE"
        return f"{estado} - {self.cliente} ({self.fecha.strftime('%d/%m %H:%M')})"        