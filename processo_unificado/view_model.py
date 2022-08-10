class ProcessoAdministrativoViewModel:

    def __init__(self):
        self.id_processo = None
        self.numero_processo = None
        self.razao_social = None
        self.cnpj = None
        self.nome_pessoa = None
        self.cpf = None
        self.numero_licenca = None
        self.tipo_licenca = None
        self.atividade = None
        self.codigo_licenca = None
        self.sigla = None
        self.data_abertura = None
        self.data_validade = None
        self.municipio = None
        self.logradouro = None
        self.numero = None

    def setModelPad(self, processo_pad):

        self.id_processo = processo_pad.id
        self.numero_processo = processo_pad.numero_processo
        self.razao_social = processo_pad.nome_pessoa_juridica
        self.cnpj = processo_pad.cnpj
        self.nome_pessoa = processo_pad.nome_pessoa_fisica
        self.cpf = processo_pad.cpf
        self.numero_licenca = processo_pad.numero_licenca
        self.atividade = processo_pad.descricao_atividade
        self.sigla = processo_pad.sigla_servico
        self.data_abertura = processo_pad.data_abertura
        self.data_validade = processo_pad.data_fim_validade
        self.municipio = processo_pad.municipio
        self.logradouro = processo_pad.logradouro
        self.numero = processo_pad.numero


    def setModelLebre(self, processo_lebre):

        self.id_processo = processo_lebre.id
        self.numero_processo = processo_lebre.numero_processo
        self.razao_social = processo_lebre.razao_social
        self.cnpj = processo_lebre.cnpj
        self.nome_pessoa = processo_lebre.nome_pessoa
        self.cpf = processo_lebre.cpf
        self.numero_licenca = processo_lebre.codigo_licenca
        self.tipo_licenca = processo_lebre.tipo_licenca
        self.sigla = processo_lebre.sigla_codigo_licenca
        self.atividade = processo_lebre.atividade
        self.data_abertura = processo_lebre.data_abertura_processo
        self.data_validade = processo_lebre.data_validade_licenca
        self.municipio = processo_lebre.municipio
        self.logradouro = processo_lebre.logradouro
        self.numero = processo_lebre



    def pass_processo_pad(self, processos):
        processo = []
        if processos:
            for p in processos:
                proc = ProcessoAdministrativoViewModel()
                proc.setModelPad(p)
                processo.append(proc)
            return processo
        return processo

    def pass_processo_lebre(self, processos):
        processo = []
        if processos:
            for p in processos:
                proc = ProcessoAdministrativoViewModel()
                proc.setModelLebre(p)
                processo.append(proc)
            return processo
        return processo






