from django.contrib import admin
from .models import Producto, CarritoDeCompras

# Register your models here.
@admin.register(CarritoDeCompras)
class CarritoDeComprasAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass