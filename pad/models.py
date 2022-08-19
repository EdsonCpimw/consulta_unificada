import datetime
import uuid

from django.db import models


class ViewProcessoAdministrativoCorporativo(models.Model):

    numero_processo = models.CharField(max_length=100)
    descricao_servico = models.TextField()
    data_abertura = models.DateField(default=datetime.datetime.now)
    sigla_servico = models.CharField(max_length=4)
    descricao_atividade = models.TextField(null=True, blank=True)
    sigla_setor = models.CharField(max_length=4, null=True, blank=True)
    nome_pessoa_fisica = models.CharField(max_length=100, null=True, blank=True)
    nome_pessoa_juridica = models.CharField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    cnpj = models.CharField(max_length=16, null=True, blank=True)
    pessoa_fisica_representante = models.CharField(max_length=100, null=True, blank=True)
    pessoa_juridica_representante = models.CharField(max_length=100, null=True, blank=True)
    numero_licenca = models.CharField(max_length=100)
    data_emissao = models.DateField(null=True, blank=True)
    data_fim_validade = models.DateField(null=True, blank=True)
    municipio = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100,  null=True, blank=True)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.id}, {self.numero_processo}'



class ViewTramitacaoCorporativo(models.Model):

    id_processo = models.IntegerField( null=True, blank=True)
    numero_processo = models.CharField(max_length=100)
    orgao_destino = models.CharField(max_length=100)
    data_envio = models.DateField(default=datetime.datetime.now)
    sigla_orgao = models.CharField(max_length=6)
    observacao = models.TextField()

    def __str__(self):
        return f'{self.id_processo}, {self.numero_processo}'

    class Meta:
        db_table = 'tb_view_tramitacao'
        ordering = ['-data_envio', ]


def upload_documento_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.id_processo}/{uuid.uuid4()}.{ext}'
    return "documentos/%s" % (filename)

class ViewDocumentosPad(models.Model):
    id_processo = models.IntegerField(null=True, blank=True)
    numero_processo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    codigo_documento = models.CharField(max_length=100)
    data_assinatura = models.DateField(default=datetime.datetime.now)
    doc_name = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=100)
    documento = models.FileField(upload_to=upload_documento_path)

    def __str__(self):
        return f'{self.id_processo}, {self.numero_processo}'

    class Meta:
        verbose_name = 'view documento'
        verbose_name_plural = 'view documentos'
        db_table = 'tb_view_documento'
        ordering = ['id', ]