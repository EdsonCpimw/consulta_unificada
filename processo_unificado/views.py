from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from lebre.models import ViewProcessoAdministrativoLebre
from pad.models import ViewProcessoAdministrativoCorporativo
from processo_unificado.filters import ConsultaPadFilter, ConsultaLebreFilter
from processo_unificado.form import ConsultaModelForm
from processo_unificado.models import Municipio
from processo_unificado.view_model import ProcessoAdministrativoViewModel


class ConsultaProcessos(ListView):
    template_name = 'processo_unificado/consulta_processos.html'
    context_object_name = 'processos'
    model = ViewProcessoAdministrativoCorporativo

    def get_context_data(self, *, object_list=None, **kwargs):
        municipios = Municipio.objects.all()
        context = super(ConsultaProcessos, self).get_context_data(**kwargs)
        context['form'] = ConsultaModelForm
        context['municipios'] = municipios
        return context

    def get_queryset(self):
        processos = []
        pad = ViewProcessoAdministrativoCorporativo.objects.all()
        lebre = ViewProcessoAdministrativoLebre.objects.all()
        if self.request.GET:
            if self.request.GET['numero_processo'] or self.request.GET['nome_interessado'] or \
                    self.request.GET['cpf_cnpj'] or self.request.GET['atividade'] or \
                    self.request.GET['numero_instrumento'] or self.request.GET['nome_municipio']:
                processos_pad = ConsultaPadFilter(self.request.GET, queryset=pad)
                processos_pad = ProcessoAdministrativoViewModel.pass_processo_pad(self, processos_pad.qs)
                processos_lebre = ConsultaLebreFilter(self.request.GET, queryset=lebre)
                processos_lebre = ProcessoAdministrativoViewModel.pass_processo_lebre(self, processos_lebre.qs)
                processos = processos_pad + processos_lebre
                return processos
        return processos



    # def get_queryset(self):
    #     numero_processo = self.request.GET.get('numero_processo', '')
    #     nome_interessado = self.request.GET.get('nome_interessado', '')
    #     cpf_cnpj = self.request.GET.get('cpf_cnpj', '')
    #     processos = []
    #     if numero_processo or nome_interessado:
    #         pad = ViewProcessoAdministrativoCorporativo.objects.filter(
    #             numero_processo__contains=numero_processo,
    #             nome_pessoa_juridica__icontains=nome_interessado,
    #             nome_pessoa_fisica__icontains=nome_interessado,
    #             cpf__contains=cpf_cnpj,
    #             cnpj__contains=cpf_cnpj
    #         )
    #         lebre = ViewProcessoAdministrativoLebre.objects.filter(numero_processo__icontains=numero_processo)
    #         # pad = ViewProcessoAdministrativoCorporativo.objects.all()
    #         # lebre = ViewProcessoAdministrativoLebre.objects.all()
    #         processos_pad = ProcessoAdministrativoViewModel.pass_processo_pad(self, pad)
    #         processos_lebre = ProcessoAdministrativoViewModel.pass_processo_lebre(self, lebre)
    #         processos = processos_pad + processos_lebre
    #         return processos
    #     return processos



    # def get_queryset(self):
    #     numero_processo = self.request.GET.get('numero_processo', None)
    #     nome_interessado = self.request.GET.get('nome_interessado', None)
    #     teste = ViewProcessoAdministrativoCorporativo.objects.all()
    #     pad = ConsultaPadFilter(self.request.GET, queryset=teste)
    #     lebre = ViewProcessoAdministrativoLebre.objects.all()
    #     processos_pad = ProcessoAdministrativoViewModel.pass_processo_pad(self, pad.qs)
    #     # processos_lebre = ProcessoAdministrativoViewModel.pass_processo_lebre(self, lebre)
    #     # processos = processos_pad + processos_lebre
    #     processos = processos_pad
    #     return processos








