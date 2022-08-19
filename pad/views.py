from django.shortcuts import render
from django.views.generic import DetailView
from pad.models import ViewProcessoAdministrativoCorporativo, ViewTramitacaoCorporativo, ViewDocumentosPad


class DetalhamentoProcesso(DetailView):
    model = ViewProcessoAdministrativoCorporativo
    template_name = 'pad/detalhamento_pad.html'
    context_object_name = 'corporativo'

    def get_context_data(self, **kwargs):
        tramitacoes = ViewTramitacaoCorporativo.objects.filter(id_processo=self.kwargs['pk']).order_by('-data_envio')
        documentos = ViewDocumentosPad.objects.filter(id_processo=self.kwargs['pk']).order_by('-data_assinatura')
        context = super(DetalhamentoProcesso, self).get_context_data(**kwargs)
        context['documentos'] = documentos
        context['tramitacoes'] = tramitacoes
        return context


