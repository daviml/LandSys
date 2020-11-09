from django import forms
from .models import Vendedores,Clientes

class LandsysFormV(forms.ModelForm):
    class Meta:
        model = Vendedores
        fileds = fields = ['cdvend','dsnome', 'cdtab', 'dtnasc']
        labels = {
            'cdvend':'Código do Vendedor',
            'dsnome':'Nome do Vendedor',
            'cdtab':'Código da tabela de preços padrão',
            'dtnasc':'Data de nascimento',
        }

class LandsysFormC(forms.ModelForm):
    class Meta:
        model = Clientes
        fileds = fields = ['cdcl','dsnome', 'idtipo', 'cdvend', 'dslim']
        labels = {
            'cdcl':'Código do Cliente',
            'dsnome':'Nome do Cliente',
            'idtipo':'Pessoa fisica ou juridica',
            'cdvend':'Código do vendedor',
            'dslim':'Limite de crédito',
        }
