from django.db import models

class Leito(models.Model):
    SALAS = [
        ('AMA', 'SALA AMARELA'),
        ('CM', 'CLINICA MÉDICA'),
        ('CC', 'CENTRO CIRÚRGICO'),
    ]
    numero = models.IntegerField(max_length=3)
    paciente = models.CharField(max_length=255, null=True)
    boletim = models.IntegerField(max_length=9, null=True)
    internacao = models.DateTimeField(null=True)
    alta = models.DateTimeField(null=True)
    sala = models.CharField(max_length=3, choices=SALAS)
    procedimento = models.TextField(blank=True, null=True)
    
