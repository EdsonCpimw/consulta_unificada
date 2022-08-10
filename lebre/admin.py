from django.contrib import admin
from lebre.models import ViewProcessoAdministrativoLebre


@admin.register(ViewProcessoAdministrativoLebre)
class ViewProcessoAdministrativoLebreAdmin(admin.ModelAdmin):
    list_display = ('numero_processo', 'id', 'tipo_licenca', 'razao_social', 'cnpj', 'nome_pessoa', 'cpf',)
    list_filter = ('numero_processo', 'razao_social', 'cnpj', 'nome_pessoa', 'cpf',)
    search_fields = ('numero_processo', 'numero_licenca', 'razao_social', 'nome_pessoa', 'cnpj',  'cpf',)
    ordering = ('id',)