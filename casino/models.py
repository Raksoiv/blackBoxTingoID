from django.db import models

# Create your models here.


class Ticket(models.Model):
    fecha_emision = models.DateField(null=True)
    fecha_expiracion = models.DateField()
    valido = models.BooleanField(default = True)
    id_ticket = models.PositiveIntegerField()
    tipo = models.CharField(max_length = 20, default = "")
    valor = models.PositiveIntegerField(default = 0)


