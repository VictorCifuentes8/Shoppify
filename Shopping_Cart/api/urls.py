from django.urls import path
from .views import CarritoView

urlpatterns = [
    path('carritoDeCompras/', CarritoView.as_view(), name='agregar_producto' ), 
]
