import re

def remove_caracteres(value):
    cnpj_cpf = re.sub('[^0-9]', '', value)
    return cnpj_cpf
