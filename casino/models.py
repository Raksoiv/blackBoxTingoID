from django.db import models

# Create your models here.


class Ticket(models.Model):
    fecha_emision = models.DateField(null=True)
    fecha_expiracion = models.DateField()
    valido = models.BooleanField(default = True)
    id_ticket = models.PositiveIntegerField()
    tipo = models.CharField(max_length = 20, default = "")
    valor = models.PositiveIntegerField(default = 0)

class Promocion(models.Model):
	fecha_expiracion =models.DateField()
	fecha_emision = models.DateField()
	meta = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=500)
	imagen = models.BinaryField(blank = True, default = None, null= True)

class Codigo_Promocion(models.Model):
	codigo = models.CharField(max_length=100)
	promocion = models.ForeignKey('Promocion')
	


