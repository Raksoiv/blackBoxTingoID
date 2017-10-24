import json
import base64
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@csrf_exempt
def detalle(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        id_ticket = json_data['id_ticket']
        try:
            print(id_ticket)
            ticket = Ticket.objects.get(id_ticket=id_ticket)
            print(ticket)
            response_data = {
                'encontrado': 'True',
                'fecha_emision': ticket.fecha_emision.isoformat(),
                'fecha_expiracion': ticket.fecha_expiracion.isoformat(),
                'valido': ticket.valido,
                'tipo': ticket.tipo,
                'valor': ticket.valor,
            }
        except ObjectDoesNotExist:
            response_data = {
            'encontrado':'False',
            'error': 'El ticket no existe'
            }


    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def discount(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf8'))
        id_ticket = json_data['id_ticket']
        try:
            ticket = Ticket.objects.get(id_ticket=id_ticket)
            if (ticket.valido=='True'):
                ticket.valido = False
                ticket.save()

            response_data = {
                'discount': 'True',
                'encontrado':'True'
            }


        except ObjectDoesNotExist:
             response_data = {
                'encontrado':'False',
                'error': 'El ticket no existe'
            }

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def promociones(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf8'))

        try:
            promociones = Promocion.objects.filter()
            if not promociones:
                response_data = []
            else:
                response_data = []
                for promocion in promociones:
                    response_data.append({
                        "promocion_id" : str(promocion.id),
                        "fecha_expiracion" : promocion.fecha_expiracion.isoformat(),
                        "fecha_emision" : promocion.fecha_emision.isoformat(),
                        "meta" : str(promocion.meta),
                        "descripcion" : promocion.descripcion,
                        "imagen" : str(base64.b64encode(promocion.imagen))
                        })
            

        except ObjectDoesNotExist:
             response_data = []

    return HttpResponse(json.dumps(response_data), content_type="application/json")

 
@csrf_exempt
def getcodigo(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf8'))
        id_promocion = str(json_data['id_promocion'])
        try:
            promocion = Promocion.objects.filter(id=id_promocion).get()
            codigo_promocion = Codigo_Promocion.objects.filter(promocion=promocion).get()
            response_data = {
                'encontrado': True,
                'codigo_promocion': str(codigo_promocion.codigo)
            }
        except ObjectDoesNotExist:
             response_data = {
                'encontrado': False
             }
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")
