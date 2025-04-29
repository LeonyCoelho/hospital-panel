from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Leito
from django.views.decorators.http import require_GET

def painel(request, sala_nome=None):
    context = {
        'sala_nome': sala_nome,  # Vai mandar o nome da sala (ou None)
    }
    return render(request, "home.html", context)

def leitos(request):
    return render(request,"leitos.html")

@require_GET
def get_all_leitos(request, sala_nome):
    # Converte o nome recebido pra caixa alta (pra evitar erro de digitação)
    sala_nome = sala_nome.upper()

    # Filtrar leitos que pertencem à sala informada (comparando o nome de exibição)
    leitos = Leito.objects.all()
    leitos_filtrados = [leito for leito in leitos if leito.get_sala_display().upper() == sala_nome]

    leitos_list = [{
        "id": leito.id,
        "numero": leito.numero,
        "paciente": leito.paciente,
        "boletim": leito.boletim,
        "internacao": leito.internacao,
        "alta": leito.alta,
        "sala": leito.get_sala_display(),
        "procedimento": leito.procedimento,
    } for leito in leitos_filtrados]

    return JsonResponse({'leitos': leitos_list})
