from django.db import models

# Create your models here.

class Municipio(models.Model):
    nome_municipio = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome_municipio}'
    def __repr__(self):
        return f'{self.nome_municipio}'

    class Meta:
        verbose_name = 'municipio'
        verbose_name_plural = 'municipios'
        db_table = 'tb_municipio'
        ordering = ['id', ]