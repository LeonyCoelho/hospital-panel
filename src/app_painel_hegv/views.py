from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Leito

def home(request):
    return render(request,"home.html")

def leitos(request):
    return render(request,"leitos.html")

def get_all_leitos(request):
    leitos = Leito.objects.all()
    leitos_list = [{
        "id": leito.id,
        "numero": leito.numero,
        "paciente": leito.paciente,
        "boletim": leito.boletim,
        "internacao": leito.internacao,
        "alta": leito.alta,
        "sala": leito.get_sala_display(),
        "procedimento": leito.procedimento,
    } for leito in leitos]
    return JsonResponse({'leitos': leitos_list})
