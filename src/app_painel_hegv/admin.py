from django.contrib import admin
from .models import Leito, SalaCirurgica, ConfiguracaoSala


@admin.register(ConfiguracaoSala)
class ConfiguracaoSalaAdmin(admin.ModelAdmin):
    list_display = ('sala', 'horas_warning', 'horas_danger')


@admin.register(Leito)
class LeitoAdmin(admin.ModelAdmin):
    list_display = ("id","numero", "sala")
    ordering = ("id",)

@admin.register(SalaCirurgica)
class SalaCirurgicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'hora_inicio', 'status', 'especialidade')
    list_filter = ('status', 'especialidade')
    search_fields = ('nome', 'especialidade')