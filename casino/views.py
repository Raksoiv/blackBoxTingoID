import json
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def detalle(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        id_ticket = json_data['id_ticket']
        ticket = Ticket.objects.filter(id_ticket=id_ticket).get()[0]
        response_data = {
            'fecha_emision': ticket.fecha_emision.isoformat(),
            'fecha_expiracion': ticket.fecha_expiracion.isoformat(),
            'valido': bool(ticket.valido),
        }
    else:
        response_data = {
            'error': 'El metodo debe ser POST'
        }

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def discount(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf8'))
        id_ticket = json_data['id_ticket']
        ticket = Ticket.objects.filter(id_ticket=id_ticket).get()[0]
        response_data = {
            'discount': bool(ticket.valido)
        }
    else:
        response_data = {
            'error': 'El metodo debe ser POST'
        }

    return HttpResponse(json.dumps(response_data), content_type="application/json")
