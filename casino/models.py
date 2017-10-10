from django.db import models

# Create your models here.


class Ticket(models.Model):
    fecha_emision = models.DateField()
    fecha_expiracion = models.DateField()
    valido = models.BooleanField()
    id_ticket = models.PositiveIntegerField()
