from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from lebre.models import ViewProcessoAdministrativoLebre


class DetalhamentoProcesso(DetailView):
    model = ViewProcessoAdministrativoLebre
    context_object_name = 'lebre'
    template_name = 'lebre/detalhamento_lebre.html'

    def get_context_data(self, **kwargs):
        context = super(DetalhamentoProcesso, self).get_context_data(**kwargs)
        return context
