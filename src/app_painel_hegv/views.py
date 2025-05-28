from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Leito, SalaCirurgica, ConfiguracaoSala
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('')  # ou pra onde quiser após login

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona após login
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')


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

@login_required(login_url='/login/')
def leitos(request, sala_nome=None):
    salas = Leito.SALAS  # lista de salas

    context = {
        'sala_nome': sala_nome,
        'salas': salas,
    }
    return render(request,"leitos.html", context)

@login_required(login_url='/login/')
def editar_leito_page(request, id, sala_nome=None):
    leito = get_object_or_404(Leito, id=id)
    salas = Leito.SALAS
    context = {
        'salas': salas,
        'sala_nome': sala_nome,
        'leito': leito
    }
    return render(request, 'leito-edit.html', context)

@login_required(login_url='/login/')
def update_leito(request, id, sala_nome=None):
    if request.method == 'POST':
        leito = get_object_or_404(Leito, id=id)

        leito.numero = request.POST.get('numero')
        leito.paciente = request.POST.get('paciente')
        leito.boletim = request.POST.get('boletim')

        internacao_str = request.POST.get('internacao')
        alta_str = request.POST.get('alta')
        leito.internacao = datetime.strptime(internacao_str, '%Y-%m-%d') if internacao_str else None
        leito.alta = datetime.strptime(alta_str, '%Y-%m-%d') if alta_str else None

        leito.sala = request.POST.get('sala')
        leito.procedimento = request.POST.get('procedimento')

        leito.save()

        # Redireciona após salvar
        return redirect(f'/leitos/{sala_nome}/')
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'}, status=400)
    
@login_required(login_url='/login/')
def create_leito(request, sala_nome=None):
    salas = Leito.SALAS
    context = {
        'salas': salas,
        'sala_nome': sala_nome,
    }
    if request.method == 'POST':
        numero = request.POST.get('numero')
        paciente = request.POST.get('paciente')
        boletim = request.POST.get('boletim')

        internacao_str = request.POST.get('internacao')
        alta_str = request.POST.get('alta')
        internacao = datetime.strptime(internacao_str, '%Y-%m-%d') if internacao_str else None
        alta = datetime.strptime(alta_str, '%Y-%m-%d') if alta_str else None

        sala = request.POST.get('sala')
        procedimento = request.POST.get('procedimento')

        Leito.objects.create(
            numero=numero,
            paciente=paciente,
            boletim=boletim,
            internacao=internacao,
            alta=alta,
            sala=sala,
            procedimento=procedimento,
        )

        messages.success(request, 'Leito criado com sucesso!')
        return redirect(f'/leitos/{sala_nome}/') 

    return render(request, 'leito-new.html', context)

@login_required(login_url='/login/')
def deletar_leito(request, id, sala_nome=None):
    leito = get_object_or_404(Leito, id=id)
    context = {
        'leito': leito,
        'sala_nome': sala_nome,
    }
    if request.method == 'POST':
        leito.delete()
        messages.success(request, 'Leito deletado com sucesso!')
        return redirect(f'/leitos/{sala_nome}/')  # redireciona para a listagem dos leitos
    
    # Se for GET, pode opcionalmente renderizar uma página ou simplesmente redirecionar
    return redirect(f'/leitos/{sala_nome}/', context)

def centro_cirurgico_view(request):
    salascc = SalaCirurgica.objects.all().order_by('nome')
    salas = Leito.SALAS  # lista de salas

    return render(request, 'centro-cirurgico.html', {'salascc': salascc, 'salas': salas})

@login_required(login_url='/login/')
def salascc(request):
    salascc = SalaCirurgica.objects.all().order_by('nome')
    salas = Leito.SALAS  # lista de salas

    return render(request, 'salascc.html', {'salascc': salascc, 'salas': salas})

@login_required(login_url='/login/')
def editar_sala_cc(request, nome):
    sala = get_object_or_404(SalaCirurgica, nome=nome)

    if request.method == 'POST':
        sala.status = request.POST.get('status')
        sala.especialidade = request.POST.get('especialidade')
        hora_inicio_str = request.POST.get('hora_inicio')
        if hora_inicio_str:
            sala.hora_inicio = datetime.strptime(hora_inicio_str, '%Y-%m-%dT%H:%M')
        else:
            sala.hora_inicio = None
        sala.save()
        return redirect('salascc')

    return render(request, 'editar-sala.html', {'sala': sala})

@login_required(login_url='/login/')
def config_salas(request):
    salas = Leito.SALAS

    if request.method == 'POST':
        for sigla, nome in salas:
            horas_warning = request.POST.get(f'warning_{sigla}')
            horas_danger = request.POST.get(f'danger_{sigla}')

            config, _ = ConfiguracaoSala.objects.get_or_create(sala=sigla)
            config.horas_warning = int(horas_warning) if horas_warning else 24
            config.horas_danger = int(horas_danger) if horas_danger else 48
            config.save()

        return redirect('config_salas')

    configs = {c.sala: c for c in ConfiguracaoSala.objects.all()}

    context = {
        'salas': salas,
        'configs': configs,
    }
    return render(request, 'config-salas.html', context)




# GET API =======================================
@require_GET
def get_all_leitos(request, sala_nome):
    # Mapeia o nome da sala para a sigla
    SALAS_MAP = {v: k for k, v in Leito.SALAS}
    sala_sigla = SALAS_MAP.get(sala_nome)

    if not sala_sigla:
        return JsonResponse({'error': 'Sala inválida'}, status=400)

    leitos = Leito.objects.filter(sala=sala_sigla).order_by('numero')

    # Busca configuração da sala, se não tiver usa padrão
    config = ConfiguracaoSala.objects.filter(sala=sala_sigla).first()

    config_data = {
        'horas_warning': config.horas_warning if config else 24,
        'horas_danger': config.horas_danger if config else 48,
    }

    leitos_list = [{
        "id": leito.id,
        "numero": leito.numero,
        "paciente": leito.paciente,
        "boletim": leito.boletim,
        "internacao": leito.internacao.strftime('%Y-%m-%dT%H:%M:%S') if leito.internacao else None,
        "alta": leito.alta.strftime('%Y-%m-%dT%H:%M:%S') if leito.alta else None,
        "sala": leito.get_sala_display(),
        "procedimento": leito.procedimento,
    } for leito in leitos]

    return JsonResponse({
        'leitos': leitos_list,
        'config': config_data,
    })



def get_leito(request, id):
    leito = Leito.objects.get(id=id)
    return JsonResponse({
        "id": leito.id,
        "numero": leito.numero,
        "paciente": leito.paciente,
        "procedimento": leito.procedimento,
    })

def api_salas_cc(request):
    salas = SalaCirurgica.objects.all().order_by('nome')
    data = []
    for sala in salas:
        data.append({
            'nome': sala.nome,
            'status': sala.status,
            'status_display': sala.get_status_display(),
            'hora_inicio': sala.hora_inicio.strftime('%Y-%m-%d %H:%M:%S') if sala.hora_inicio else None,
            'especialidade': sala.especialidade,
        })
    return JsonResponse({'salascc': data})