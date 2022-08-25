from django.contrib import admin
from lebre.models import ViewProcessoAdministrativoLebre, ViewNotificacoesLebre, ViewVistoriaLebre, ViewTramitacaoLebre, \
    ViewDespachoLebre, ViewPareceresArquivosLebre


@admin.register(ViewProcessoAdministrativoLebre)
class ViewProcessoAdministrativoLebreAdmin(admin.ModelAdmin):
    list_display = ('numero_processo', 'id', 'tipo_licenca', 'razao_social', 'cnpj', 'nome_pessoa', 'cpf',)
    list_filter = ('numero_processo', 'razao_social', 'cnpj', 'nome_pessoa', 'cpf',)
    search_fields = ('numero_processo', 'numero_licenca', 'razao_social', 'nome_pessoa', 'cnpj',  'cpf',)
    ordering = ('id',)


@admin.register(ViewNotificacoesLebre)
class ViewNotificacaoLebreAdmin(admin.ModelAdmin):
    list_display = ('id_processo', 'id', 'codigo_numero', 'data_emissao', 'tipo_aviso', 'descricao_sigla', 'descricao_assunto',)
    list_filter = ('id_processo', 'codigo_numero', 'data_emissao', 'tipo_aviso')
    search_fields = ('id_processo', 'tipo_aviso', 'codigo_numero',)
    ordering = ('id',)


@admin.register(ViewVistoriaLebre)
class ViewVistoriaLebreAdmin(admin.ModelAdmin):
    list_display = ('id_processo', 'id', 'numero_vistoria', 'data_vistoria', 'id_vistoria', 'descricao',)
    list_filter = ('id_processo', 'numero_vistoria', 'data_vistoria',)
    search_fields = ('id_processo', 'numero_vistoria',)
    ordering = ('id',)


@admin.register(ViewPareceresArquivosLebre)
class ViewPareceresArquivosLebreAdmin(admin.ModelAdmin):
    list_display = ('id_processo', 'id', 'descricao_documento', 'descricao_usuario', 'data_emissao', 'descricao',)
    list_filter = ('id_processo', 'descricao_documento', 'descricao_usuario',)
    search_fields = ('id_processo', 'numero_vistoria',)
    ordering = ('id',)


@admin.register(ViewTramitacaoLebre)
class ViewTramitacaoLebreAdmin(admin.ModelAdmin):
    list_display = ('id_processo', 'id', 'orgao_origem', 'data_remessa', 'setor_destino', 'data_recebimento', 'despacho',)
    list_filter = ('id_processo', 'orgao_origem', 'setor_destino',)
    search_fields = ('id_processo', 'orgao_origem',)
    ordering = ('id',)


@admin.register(ViewDespachoLebre)
class ViewDespacho(admin.ModelAdmin):
    list_display = ('id_processo', 'id', 'origem', 'destino', 'data_despacho', 'data_conclusao', 'despacho',)
    list_filter = ('id_processo', 'origem', 'destino',)
    search_fields = ('id_processo', 'origem',)
    ordering = ('id',)