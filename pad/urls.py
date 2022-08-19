from django.urls import path
from pad.views import DetalhamentoProcesso

app_name = 'pad'

urlpatterns = [
    path('<int:pk>/detalhamento/', DetalhamentoProcesso.as_view(), name='detalhamento')
]