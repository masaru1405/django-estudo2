from django.urls import path
from . import views

urlpatterns = [
   path('', views.welcome, name='welcome'),
   path('contas/', views.contas, name='contas'),
   path('listagem/', views.listagem, name='listagem'),
   path('nova_transacao/', views.nova_transacao, name='nova_transacao'),
   path('update/<int:id>/', views.update, name='update'),
]