import json
import blackbox.settings as settings
from .models import Ticket
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        if json_data['user'] == 'TingoID' and json_data['password'] == '1234':
            json_data = {'token': '12345678'}
        else:
            json_data = {'error': 'nombre usuario/password incorrecta'}
    else:
        json_data = {'error': 'El metodo debe ser POST'}
    return HttpResponse(json.dumps(json_data), content_type='application/json')


@csrf_exempt
def check(request):

    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        ticket = Ticket.objects.get(pk=json_data['codigoEntradaText'])
        response_data = {
            'idRegistro': ticket.id,
            'fecha_exp': str(ticket.fecha_exp),
            'estado': ticket.estado,
            'costo': ticket.costo,
            'detalle': ticket.detalle,
            'empresa': settings.NOMBRE_EMPRESA
        }
    else:
        response_data = {
            'error': 'El metodo debe ser POST'
        }

    return HttpResponse(json.dumps(response_data), content_type="application/json")
