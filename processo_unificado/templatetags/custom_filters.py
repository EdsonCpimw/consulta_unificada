from django import template
register = template.Library()

@register.filter(name='cpf')
def filter_cpf(value):
    cpf = value
    cpf = ''.join((cpf[:3], '.', cpf[3:6], '.', cpf[6:9], '-', cpf[9:11]))
    return cpf

@register.filter(name='cnpj')
def filter_cnpj(value):
    cnpj = value
    cnpj = ''.join((cnpj[:2], '.', cnpj[2:5], '.', cnpj[5:8], '/', cnpj[8:12], '-', cnpj[12:14]))
    return cnpj



