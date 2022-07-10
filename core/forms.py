from django import forms
from core.models import Item, Orcamento

class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        exclude = ['ativo']

class OrcamentoForm(forms.ModelForm):
    
    class Meta:
        model = Orcamento
        exclude = ['ativo', 'pessoa', 'pessoa_info']