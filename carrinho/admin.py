# carrinho/admin.py
from django.contrib import admin
from .models import ItemCarrinho, Compra

@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'produto', 'quantidade', 'preco_unitario', 'subtotal')
    search_fields = ('cliente__nome', 'produto__nome')

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'valor_total')
    search_fields = ('cliente__nome',)
