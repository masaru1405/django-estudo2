from django.shortcuts import render


def home(request):
   data = dict(nome='Kaio', idade=37, nacionalidade='brasileiro', frutas=['melancia', 'banana', 'laranja'])
   return render(request, 'contas/home.html', data)
