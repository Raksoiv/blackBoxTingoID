import json
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
                'valido': bool(ticket.valido),
                'tipo': char(ticket.tipo),
                'valor': int(ticket.valor),
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
            if (bool(ticket.valido)):
                ticket.valido = False
                ticket.save()

            response_data = {
                'discount': bool(ticket.valido),
                'encontrado':'True'
            }


        except ObjectDoesNotExist:
             response_data = {
                'encontrado':'False',
                'error': 'El ticket no existe'
            }

    return HttpResponse(json.dumps(response_data), content_type="application/json")
