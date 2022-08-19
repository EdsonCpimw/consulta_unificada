import django_filters
from lebre.models import ViewProcessoAdministrativoLebre
from utils.regex import remove_caracteres


class ConsultaLebreFilter(django_filters.FilterSet):
    numero_processo = django_filters.CharFilter(field_name='numero_processo', lookup_expr='contains')
    nome_interessado = django_filters.CharFilter(method='filter_nome_interessado')
    cpf_cnpj = django_filters.CharFilter(method='filter_cpf_cnpj')
    atividade = django_filters.CharFilter(field_name='atividade', lookup_expr='contains')
    numero_instrumento = django_filters.CharFilter(field_name='codigo_licenca', lookup_expr='icontains')
    nome_municipio = django_filters.CharFilter(field_name='municipio', lookup_expr='contains')

    def filter_nome_interessado(self, queryset, name, value):
         juridica = queryset.filter(razao_social__icontains=value)
         fisica = queryset.filter(nome_pessoa__icontains=value)
         if juridica:
             return juridica

         else:
             return fisica

    def filter_cpf_cnpj(self, queryset, name, value):
        cpf_cnpj = remove_caracteres(value)
        if len(cpf_cnpj) == 11:
           return queryset.filter(cpf__contains=cpf_cnpj)

        else:
            return queryset.filter(cnpj__contains=cpf_cnpj)

    class Meta:
        model = ViewProcessoAdministrativoLebre
        fields = ('numero_processo', 'atividade', 'codigo_licenca', 'municipio',)