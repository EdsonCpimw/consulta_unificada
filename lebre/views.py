from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView


class DetalhamentoProcesso(TemplateView):
    template_name = 'lebre/detalhamento_lebre.html'
