from django.db import models

# Create your models here.


class Ticket(models.Model):
    fecha_exp = models.DateField()
    estado = models.CharField(max_length=10)
    costo = models.IntegerField()
    detalle = models.CharField(max_length=200)
