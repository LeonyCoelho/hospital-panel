from django.contrib import admin
from .models import Leito

@admin.register(Leito)
class LeitoAdmin(admin.ModelAdmin):
    list_display = ("id","numero", "sala")
    ordering = ("id",)
