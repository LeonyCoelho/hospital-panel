from django.db import models
from django.core.validators import MaxValueValidator

class ConfiguracaoSala(models.Model):
    sala = models.CharField(max_length=3, choices=[
        ('AMA', 'SALA AMARELA'),
        ('MIS', 'SALA VERDE MISTA'),
        ('CIR', 'CLINICA CIRÚRGICA'),
    ], unique=True)

    horas_warning = models.IntegerField(default=24, help_text="Horas para passar de success para warning")
    horas_danger = models.IntegerField(default=48, help_text="Horas para passar de warning para danger")

    def __str__(self):
        return f"Config {self.get_sala_display()}"

class Leito(models.Model):
    SALAS = [
        ('AMA', 'SALA AMARELA'),
        ('MIS', 'SALA VERDE MISTA'),
        ('CIR', 'CLINICA CIRÚRGICA'),
    ]
    numero = models.IntegerField(validators=[MaxValueValidator(999999)],unique=True)
    paciente = models.CharField(max_length=255, null=True)
    boletim = models.IntegerField(validators=[MaxValueValidator(999999)], unique=True, null=True)
    internacao = models.DateTimeField(null=True)
    alta = models.DateTimeField(null=True)
    sala = models.CharField(max_length=3, choices=SALAS)
    procedimento = models.TextField(blank=True, null=True)
    
class SalaCirurgica(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('cirurgia', 'Em Cirurgia'),
        ('higienizacao', 'Em Higienização'),
    ]

    nome = models.CharField(max_length=20, unique=True)  # Ex: SALA 1, SALA 2, etc
    hora_inicio = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='vazia')
    especialidade = models.CharField(max_length=100, blank=True, null=True)  # livre, pode adaptar depois

    def __str__(self):
        return f'{self.nome} - {self.get_status_display()}'
