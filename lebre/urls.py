from django.urls import path
from lebre.views import DetalhamentoProcesso

app_name = 'lebre'

urlpatterns = [
    path('detalhamento/', DetalhamentoProcesso.as_view(), name='detalhamento')
]