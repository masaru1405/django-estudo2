from django.shortcuts import render
from .models import Transacao

def home(request):
   data = dict(nome='Kaio', idade=37, nacionalidade='brasileiro', frutas=['melancia', 'banana', 'laranja'])
   return render(request, 'contas/home.html', data)

def listagem(request):
   data = dict(transacoes = Transacao.objects.all)
   return render(request, 'contas/listagem.html', data)