from django.shortcuts import render
from django.views.generic import ListView, DetailView

from lebre.models import ViewProcessoAdministrativoLebre
from pad.models import ViewProcessoAdministrativoCorporativo
from processo_unificado.view_model import ProcessoAdministrativoViewModel


class ConsultaProcessos(ListView):
    template_name = 'processo_unificado/consulta_processos.html'
    context_object_name = 'processos'

    def get_queryset(self):
        # pad = ViewProcessoAdministrativoCorporativo.objects.filter(numero_processo__exact='E-07/002.3622/2014')
        # lebre = ViewProcessoAdministrativoLebre.objects.filter(numero_processo__exact='E-07/002.3622/2014')
        pad = ViewProcessoAdministrativoCorporativo.objects.all()
        lebre = ViewProcessoAdministrativoLebre.objects.all()
        processos_pad = ProcessoAdministrativoViewModel.pass_processo_pad(self, pad)
        processos_lebre = ProcessoAdministrativoViewModel.pass_processo_lebre(self, lebre)
        processos = processos_pad + processos_lebre
        return processos
