from django.contrib import admin
from pad.models import ViewProcessoAdministrativoCorporativo


@admin.register(ViewProcessoAdministrativoCorporativo)
class ViewProcessoAdministrativoAdmin(admin.ModelAdmin):
    list_display = ('numero_processo', 'id', 'numero_licenca', 'nome_pessoa_juridica', 'cnpj', 'nome_pessoa_fisica', 'cpf',)
    list_filter = ('numero_processo', 'nome_pessoa_juridica', 'nome_pessoa_fisica',)
    search_fields = ('numero_processo', 'numero_licenca', 'nome_pessoa_juridica', 'nome_pessoa_fisica', 'cnpj',  'cpf',)
    ordering = ('id',)
