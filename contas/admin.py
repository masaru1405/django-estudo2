from django.contrib import admin
from .models import Categoria, Transacao

admin.site.register(Categoria)
admin.site.register(Transacao)

# @admin.register(Categoria)
# class CategoriaAdmin(admin.ModelAdmin):
#    list_display = ['nome', 'dt_criacao']
