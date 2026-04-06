# 🧼 Mundo Limpieza 526 - Sistema de Gestión y E-commerce

Este es un proyecto de **Backend Developer** diseñado para la gestión de inventario y ventas de un local de artículos de limpieza en **La Plata (Calle 526)**. La plataforma permite a los usuarios navegar por un catálogo dinámico y realizar pedidos directamente a través de **WhatsApp**.

## 🚀 Demo En Vivo
Puedes ver el proyecto funcionando aquí: 
[mundolimpieza526.pythonanywhere.com](https://mundolimpieza526.pythonanywhere.com/)

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10
* **Framework Web:** Django (MTV Architecture)
* **Base de Datos:** SQLite (Desarrollo y Producción inicial)
* **Frontend:** HTML5, CSS3 (Bootstrap), JavaScript
* **Despliegue:** PythonAnywhere
* **Control de Versiones:** Git & GitHub

---

## ✨ Características Principales

* **Catálogo Dinámico:** Los productos se cargan desde el panel administrativo de Django.
* **Gestión de Stock:** Panel de control para el administrador (Analista/Dueño) donde puede realizar CRUD (Crear, Leer, Actualizar, Borrar) de productos.
* **Integración con WhatsApp:** El carrito de compras genera un mensaje automático con el detalle del pedido para el vendedor, facilitando la logística local.
* **Diseño Responsive:** Optimizado para dispositivos móviles, pensando en los clientes que realizan pedidos rápidos.
* **Arquitectura de Datos:** Modelos de datos optimizados para categorías, precios y disponibilidad.

---

## 📂 Estructura del Proyecto

* `tienda_limpieza/`: Configuración principal del proyecto (settings, urls, wsgi).
* `productos/`: Aplicación principal que maneja los modelos de productos y vistas del catálogo.
* `static/`: Archivos CSS, imágenes de diseño y JavaScript.
* `media/`: Imágenes de los productos cargadas por el administrador.
* `manage.py`: Script de gestión de Django.

---

## 🔧 Instalación Local

Si quieres correr este proyecto en tu máquina:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/ridermanriquecueto/tienda-limpieza.git](https://github.com/ridermanriquecueto/tienda-limpieza.git)

   Crear y activar entorno virtual:

Bash
python -m venv env
# En Windows:
env\Scripts\activate
Instalar dependencias:

Bash
pip install django pillow
Correr migraciones y servidor:

Bash
python manage.py migrate
python manage.py runserver