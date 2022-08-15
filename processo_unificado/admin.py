from django.contrib import admin

# Register your models here.
from processo_unificado.models import Municipio


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nome_municipio', 'id',)
    list_filter = ('nome_municipio',)
    ordering = ('id',)