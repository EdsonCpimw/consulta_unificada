import re

def remove_caracteres(cnpj_cpf):
    teste = re.sub('[^0-9]', '', cnpj_cpf)
    return teste
