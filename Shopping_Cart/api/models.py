from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    categoria = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

class CarritoDeCompras(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, to_field="id")
    cantidad = models.IntegerField(default=1)