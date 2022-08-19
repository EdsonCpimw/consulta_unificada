from django import forms
from processo_unificado.models import Municipio



class ConsultaModelForm(forms.Form):

    numero_processo = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Numero do Processo"}
    ))
    nome_interessado = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Nome do Interessado"}
    ))
    cpf_cnpj = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control cpfcnpj', 'placeholder': "CPF OU CNPJ"}
    ))
    atividade = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Atividade"}
    ))
    numero_instrumento = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Numero do Instrumento"}
    ))
    nome_municipio = forms.ModelChoiceField(required=False, empty_label='Selecione', to_field_name='nome_municipio',
        queryset=Municipio.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control select2', }))
