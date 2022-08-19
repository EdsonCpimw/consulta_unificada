from django.urls import path
from processo_unificado.views import ConsultaProcessos

app_name = 'consulta'

urlpatterns = [
    path('processos/', ConsultaProcessos.as_view(), name='unificada')
]