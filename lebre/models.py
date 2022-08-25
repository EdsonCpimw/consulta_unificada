import uuid
from django.db import models
import datetime


def upload_pareceres_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.id_processo}/{uuid.uuid4()}.{ext}'
    return "pareceres/%s" % (filename)

def upload_notificacao_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.id_processo}/{uuid.uuid4()}.{ext}'
    return "notificacao/%s" % (filename)

def upload_vistoria_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.id_processo}/{uuid.uuid4()}.{ext}'
    return "vistoria/%s" % (filename)


class ViewProcessoAdministrativoLebre(models.Model):
    numero_processo = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100, null=True, blank=True)
    cnpj = models.CharField(max_length=16, null=True, blank=True)
    nome_pessoa = models.CharField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    data_abertura_processo = models.DateField(default=datetime.datetime.now)
    codigo_licenca = models.CharField(max_length=50)
    data_emissao_licenca = models.DateField(null=True, blank=True)
    data_validade_licenca = models.DateField(null=True, blank=True)
    tipo_licenca = models.CharField(max_length=100, null=True, blank=True)
    sigla_codigo_licenca = models.CharField(max_length=2, null=True, blank=True)
    logradouro = models.CharField(max_length=100, null=True, blank=True)
    municipio = models.CharField(max_length=100, null=True, blank=True)
    estado_endereco_instalacao = models.CharField(max_length=100, null=True, blank=True)
    atividade = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}, {self.numero_processo}'


class ViewNotificacoesLebre(models.Model):
    id_processo = models.IntegerField()
    codigo_numero = models.CharField(max_length=100, null=True,blank=True)
    data_emissao = models.DateField(default=datetime.datetime.now)
    tipo_aviso = models.CharField(max_length=100)
    descricao_assunto = models.CharField(max_length=150)
    descricao_sigla = models.CharField(max_length=100)
    documento_notificacao = models.FileField(upload_to=upload_notificacao_path)

    def __str__(self):
        return f'{self.id}, {self.id_processo}, {self.codigo_numero}'

    class Meta:
        verbose_name = 'view notificação'
        verbose_name_plural = 'view notificações'
        db_table = 'tb_view_notificacao'
        ordering = ['id', ]


class ViewVistoriaLebre(models.Model):
    id_processo = models.IntegerField()
    numero_vistoria = models.CharField(max_length=100)
    data_vistoria = models.DateField(default=datetime.datetime.now)
    descricao = models.CharField(max_length=150)
    id_vistoria = models.IntegerField()
    documento_vistoria = models.FileField(upload_to=upload_vistoria_path)

    def __str__(self):
        return f'{self.id}, {self.numero_vistoria}'

    class Meta:
        verbose_name = 'view vistoria'
        verbose_name_plural = 'view vistorias'
        db_table = 'tb_view_vistoria'
        ordering = ['id', ]


class ViewPareceresArquivosLebre(models.Model):
    id_processo = models.IntegerField()
    descricao_documento = models.CharField(max_length=150)
    arquivo_parecer = models.FileField(upload_to=upload_pareceres_path)
    data_emissao = models.DateField(default=datetime.datetime.now)
    descricao_usuario = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.id}, {self.descricao_documento}'

    class Meta:
        verbose_name = 'view pareceres e arquivos'
        verbose_name_plural = 'view pareceres arquivos'
        db_table = 'tb_view_pareceres_arquivos'
        ordering = ['id', ]


class ViewTramitacaoLebre(models.Model):
    id_processo = models.IntegerField()
    tipo = models.CharField(max_length=100)
    orgao_origem = models.CharField(max_length=6)
    data_remessa = models.DateField(default=datetime.datetime.now)
    setor_destino = models.CharField(max_length=100)
    data_recebimento = models.DateField(default=datetime.datetime.now)
    despacho = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.id}, {self.id_processo}'

    class Meta:
        verbose_name = 'view tramitacao'
        verbose_name_plural = 'view tramitacoes'
        db_table = 'tb_view_tramitacao'
        ordering = ['id', ]


class ViewDespachoLebre(models.Model):
    id_processo = models.IntegerField()
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_despacho = models.DateField(default=datetime.datetime.now)
    data_conclusao = models.DateField(default=datetime.datetime.now)
    despacho = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.id}, {self.id_processo}'

    class Meta:
        verbose_name = 'view depacho'
        verbose_name_plural = 'view despachos'
        db_table = 'tb_view_despacho'
        ordering = ['id', ]






