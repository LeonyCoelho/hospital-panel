from django.contrib import admin
from .models import Leito, SalaCirurgica

@admin.register(Leito)
class LeitoAdmin(admin.ModelAdmin):
    list_display = ("id","numero", "sala")
    ordering = ("id",)

@admin.register(SalaCirurgica)
class SalaCirurgicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'hora_inicio', 'status', 'especialidade')
    list_filter = ('status', 'especialidade')
    search_fields = ('nome', 'especialidade')