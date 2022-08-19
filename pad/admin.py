from django.contrib import admin

from pad.models import (ViewProcessoAdministrativoCorporativo,
                        ViewTramitacaoCorporativo,
                        ViewDocumentosPad, )


@admin.register(ViewProcessoAdministrativoCorporativo)
class ViewProcessoAdministrativoAdmin(admin.ModelAdmin):
    list_display = ('numero_processo', 'id', 'numero_licenca', 'nome_pessoa_juridica', 'cnpj', 'nome_pessoa_fisica',
                    'cpf',)
    list_filter = ('numero_processo', 'nome_pessoa_juridica', 'nome_pessoa_fisica',)
    search_fields = ('numero_processo', 'numero_licenca', 'nome_pessoa_juridica', 'nome_pessoa_fisica', 'cnpj',  'cpf',)
    ordering = ('id',)


@admin.register(ViewTramitacaoCorporativo)
class ViewTramitacaoCorporativoAdmin(admin.ModelAdmin):
    list_display = ('numero_processo', 'id', 'orgao_destino', 'sigla_orgao', 'data_envio', 'observacao',)
    list_filter = ('numero_processo', 'data_envio', 'sigla_orgao',)
    search_fields = ('numero_processo', 'sigla_orgao',)
    ordering = ('id',)


@admin.register(ViewDocumentosPad)
class ViewDocumentosPadAdmin(admin.ModelAdmin):
    list_display = ('numero_processo', 'id', 'autor', 'codigo_documento', 'tipo_documento', 'data_assinatura',
                    'documento',)
    list_filter = ('numero_processo', 'data_assinatura', 'codigo_documento', 'tipo_documento',)
    search_fields = ('numero_processo', 'codigo_documento', 'tipo_documento',)
    ordering = ('id',)