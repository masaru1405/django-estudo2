from django.shortcuts import render,redirect
from .models import Transacao
from .form import TransacaoForm

def welcome(request):
   return render(request, 'contas/welcome.html')

def contas(request):
   data = dict(nome='Kaio', idade=37, nacionalidade='brasileiro', frutas=['melancia', 'banana', 'laranja'])
   return render(request, 'contas/contas.html', data)

def listagem(request):
   data = dict(transacoes = Transacao.objects.all)
   return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
   data = dict(form=TransacaoForm(request.POST or None))
   if data['form'].is_valid():
      data['form'].save()
      return redirect('listagem') #volta para a página listagem
   return render(request, 'contas/form.html', data)

def update(request, id):
   transacao = Transacao.objects.get(pk=id)
   data = dict(form=TransacaoForm(request.POST or None, instance=transacao))
   if data['form'].is_valid():
      data['form'].save()
      return redirect('listagem')
   return render(request, 'contas/form.html', data)