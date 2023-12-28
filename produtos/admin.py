from django.contrib import admin
from .models import Produto,Categoria

@admin.register(Categoria)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
@admin.register(Produto)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao','preco','estoque','data_de_vencimento')
    search_fields = ('nome','preco')


