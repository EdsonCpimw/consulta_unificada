from django.db import models
import datetime

# Create your models here.


class ViewProcessoAdministrativoLebre(models.Model):

    numero_processo = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100, null=True, blank=True)
    cnpj = models.CharField(max_length=16)
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