from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Caja)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Marca)
admin.site.register(Descuento)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Pedido)