from django.forms import ModelForm
from .models import Transacao, Categoria

class TransacaoForm(ModelForm):
   class Meta:
      model =  Transacao
      fields = ['data', 'descricao', 'valor', 'categoria', 'observacoes']

class CategoriaForm(ModelForm):
   class Meta:
      model = Categoria
      fields = ['nome']