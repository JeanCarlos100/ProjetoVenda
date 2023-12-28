# produtos/views.py
from django.shortcuts import render
from .models import Produto
from datetime import date

def lista_produtos(request):
    produtos = Produto.objects.filter(data_de_vencimento__gte=date.today(), estoque__gt=0)
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})
