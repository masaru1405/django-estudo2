from django.urls import path
from . import views

urlpatterns = [
   path('', views.welcome, name='welcome'),
   path('contas/', views.contas, name='contas'),
   path('listagem/', views.listagem, name='listagem'),
   path('nova_transacao/', views.nova_transacao, name='nova_transacao'),
   path('update/<int:id>/', views.update, name='update'),
   path('delete/<int:id>/', views.delete, name='delete'),

   path('nova_categoria/', views.nova_categoria, name='nova_categoria'),
   path('listagem_categorias/', views.listagem_categorias, name='listagem_categorias'),
]