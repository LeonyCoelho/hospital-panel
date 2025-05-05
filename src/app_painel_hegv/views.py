from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Leito
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


def home(request, sala_nome=None):
    salas = Leito.SALAS  # lista de salas

    context = {
        'sala_nome': sala_nome,
        'salas': salas,
    }
    return render(request,"home.html", context)

def painel(request, sala_nome=None):
    salas = Leito.SALAS  # lista de salas

    context = {
        'sala_nome': sala_nome,
        'salas': salas,
    }
    return render(request, "painel.html", context)

def leitos(request, sala_nome=None):
    salas = Leito.SALAS  # lista de salas

    context = {
        'sala_nome': sala_nome,
        'salas': salas,
    }
    return render(request,"leitos.html", context)

def novo_leito(request):
    return render(request, 'leito-new.html')

def editar_leito_page(request, id):
    leito = get_object_or_404(Leito, id=id)
    return render(request, 'leito-edit.html', {'leito': leito})

def update_leito(request, id):
    if request.method == 'POST':
        leito = get_object_or_404(Leito, id=id)

        leito.numero = request.POST.get('numero')
        leito.paciente = request.POST.get('paciente')
        leito.boletim = request.POST.get('boletim')

        # Conversão segura das datas (padrão yyyy-mm-dd do input type="date")
        internacao_str = request.POST.get('internacao')
        alta_str = request.POST.get('alta')
        leito.internacao = datetime.strptime(internacao_str, '%Y-%m-%d') if internacao_str else None
        leito.alta = datetime.strptime(alta_str, '%Y-%m-%d') if alta_str else None

        leito.sala = request.POST.get('sala')
        leito.procedimento = request.POST.get('procedimento')

        leito.save()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'}, status=400)

@csrf_exempt  # Só se necessário. Prefira usar {% csrf_token %} no form e manter CSRF ON.
def novo_leito_form(request):
    if request.method == 'POST':
        leito = Leito(
            numero=request.POST.get('numero'),
            paciente=request.POST.get('paciente'),
            boletim=request.POST.get('boletim'),
            internacao=request.POST.get('internacao'),
            alta=request.POST.get('alta'),
            sala=request.POST.get('sala'),
            procedimento=request.POST.get('procedimento'),
        )
        leito.save()
        return redirect('/painel/')  # ou outro destino
    return render(request, 'leito-new.html')

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


def get_leito(request, id):
    leito = Leito.objects.get(id=id)
    return JsonResponse({
        "id": leito.id,
        "numero": leito.numero,
        "paciente": leito.paciente,
        "procedimento": leito.procedimento,
    })