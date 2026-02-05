from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from productos import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('pedido/', views.pedido, name='pedido'),
    path('contacto/', views.contacto, name='contacto'),
    path('guardar-pedido/', views.guardar_pedido, name='guardar_pedido'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)