# carrinho/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ItemCarrinho, Compra
from .forms import SelecaoProdutoForm
from .models import Produto
from .forms import SelecaoClienteForm

@login_required
def selecionar_produtos(request):
    if request.method == 'POST':
        form = SelecaoClienteForm(request.POST)
        if form.is_valid():
            cliente_selecionado = form.cleaned_data['cliente']
            # Adicione a lógica necessária para selecionar produtos com base no cliente selecionado
            return redirect('sua_view_para_exibir_produtos', cliente_id=cliente_selecionado.id)
    else:
        form = SelecaoClienteForm()

    return render(request, 'carrinho/selecionar_produtos.html', {'form': form})

@login_required
def selecionar_produtos(request):
    cliente = request.user.cliente
    produtos_disponiveis = Produto.objects.filter(disponivel=True)
    
    if request.method == 'POST':
        form = SelecaoProdutoForm(request.POST)
        if form.is_valid():
            quantidade = form.cleaned_data['quantidade']
            produto = form.cleaned_data['produto']
            
            # Verifica se já existe um item para esse produto no carrinho
            item, created = ItemCarrinho.objects.get_or_create(cliente=cliente, produto=produto)
            
            # Atualiza a quantidade e salva
            item.quantidade += quantidade
            item.save()

            return redirect('selecionar_produtos')
    else:
        form = SelecaoProdutoForm(queryset=produtos_disponiveis)
    
    return render(request, 'carrinho/selecionar_produtos.html', {'form': form})

@login_required
def visualizar_compras(request):
    cliente = request.user.cliente
    compras = Compra.objects.filter(cliente=cliente)
    return render(request, 'carrinho/visualizar_compras.html', {'compras': compras})
