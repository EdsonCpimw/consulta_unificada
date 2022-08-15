import django_filters
from pad.models import ViewProcessoAdministrativoCorporativo
from utils.regex import remove_caracteres


class ConsultaPadFilter(django_filters.FilterSet):
    numero_processo = django_filters.CharFilter(field_name='numero_processo', lookup_expr='contains')
    nome_interessado = django_filters.CharFilter(field_name='nome_pessoa_juridica', method='filter_nome_interessado')
    # nome_interessado = django_filters.CharFilter(field_name='nome_pessoa_fisica', lookup_expr='icontains')
    cpf_cnpj = django_filters.CharFilter(field_name='cnpj',  method='filter_cpf_cnpj')
    # cpf = django_filters.CharFilter(field_name='cpf_cnpj', lookup_expr='exact', required=False)
    atividade = django_filters.CharFilter(field_name='descricao_atividade', lookup_expr='icontains')
    numero_instrumento = django_filters.CharFilter(field_name='numero_licenca', lookup_expr='icontains')
    nome_municipio = django_filters.CharFilter(field_name='municipio', lookup_expr='contains')

    def filter_cpf_cnpj(self, queryset, name, value):
        cpf_cnpj = remove_caracteres(value)
        print(cpf_cnpj)
        if len(cpf_cnpj) == 11:
           return queryset.filter(cpf__contains=cpf_cnpj)

        else:
            return queryset.filter(cnpj__contains=cpf_cnpj)

    def filter_nome_interessado(self, queryset, name, value):
         juridica = queryset.filter(nome_pessoa_juridica__icontains=value)
         fisica = queryset.filter(nome_pessoa_fisica__icontains=value)
         if juridica:
             return juridica

         else:
             return fisica

    class Meta:
        model = ViewProcessoAdministrativoCorporativo
        fields = ('numero_processo', 'descricao_atividade', 'numero_licenca', 'municipio',)