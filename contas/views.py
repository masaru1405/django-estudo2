from django.shortcuts import render,redirect
from .models import Transacao, Categoria
from .form import TransacaoForm, CategoriaForm

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
   #Obs: data['id_para_deletar'] é para ser usado com delete no form.html (line 17). Ver vídeo: https://www.youtube.com/watch?v=4HuWCNf0UyI
   data = dict(form=TransacaoForm(request.POST or None, instance=transacao), id_para_deletar=transacao)
   if data['form'].is_valid():
      data['form'].save()
      return redirect('listagem')
   return render(request, 'contas/form.html', data)

def delete(request, id):
   transacao = Transacao.objects.get(pk=id)
   transacao.delete()
   return redirect('listagem')

def listagem_categorias(request):
   data = dict(categorias=Categoria.objects.all)
   return render(request, 'contas/categorias.html', data)

def nova_categoria(request):
   data = dict(form=CategoriaForm(request.POST or None))
   if data['form'].is_valid():
      data['form'].save()
      return redirect('listagem_categorias')
   return render(request, 'contas/form_categoria.html', data)