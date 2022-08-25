from django.shortcuts import render
from django.views.generic import DetailView
from lebre.models import ViewProcessoAdministrativoLebre, ViewNotificacoesLebre, ViewVistoriaLebre, \
    ViewPareceresArquivosLebre, ViewTramitacaoLebre, ViewDespachoLebre


class DetalhamentoProcesso(DetailView):
    model = ViewProcessoAdministrativoLebre
    context_object_name = 'lebre'
    template_name = 'lebre/detalhamento_lebre.html'

    def get_context_data(self, **kwargs):
        notificacoes = ViewNotificacoesLebre.objects.filter(id_processo=self.kwargs['pk'])
        vistorias = ViewVistoriaLebre.objects.filter(id_processo=self.kwargs['pk'])
        pareceres = ViewPareceresArquivosLebre.objects.filter(id_processo=self.kwargs['pk'])
        tramitacoes = ViewTramitacaoLebre.objects.filter(id_processo=self.kwargs['pk'])
        despachos = ViewDespachoLebre.objects.filter(id_processo=self.kwargs['pk'])
        context = super(DetalhamentoProcesso, self).get_context_data(**kwargs)
        context['notificacoes'] = notificacoes
        context['vistorias'] = vistorias
        context['pareceres'] = pareceres
        context['tramitacoes'] = tramitacoes
        context['despachos'] = despachos
        return context
