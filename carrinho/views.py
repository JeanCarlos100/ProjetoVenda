from django.shortcuts import render
from .models import ItemCarrinho, Compra
from Cliente.models import Cliente
from produtos.models import Produto
# Importe a classe MultipleObjectsReturned
from django.core.exceptions import MultipleObjectsReturned

#@receiver(post_save, sender=ItemCarrinho)
def atualizar_valor_total_compra(sender, instance, **kwargs):
    try:
        # Tente obter uma única compra para o cliente
        compra = Compra.objects.get(cliente=instance.cliente)
    except Compra.DoesNotExist:
        # Se não existir, crie uma nova
        compra = Compra(cliente=instance.cliente)
    except MultipleObjectsReturned:
        # Se houver mais de uma compra, pegue a primeira (ou ajuste conforme necessário)
        compra = Compra.objects.filter(cliente=instance.cliente).first()

    # Atualize o valor total da compra
    compra.valor_total = sum(item.subtotal for item in ItemCarrinho.objects.filter(cliente=instance.cliente))
    compra.save()

def adicionar_carrinho(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        produto_id = request.POST.get('produto')
        quantidade = int(request.POST.get('quantidade', 1))

        cliente = Cliente.objects.get(id=cliente_id)
        produto = Produto.objects.get(id=produto_id)

        item_carrinho, created = ItemCarrinho.objects.get_or_create(cliente=cliente, produto=produto)
        item_carrinho.quantidade += quantidade
        item_carrinho.save()

    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'carrinho/carrinho_form.html', {'clientes': clientes, 'produtos': produtos})

def listar_compras(request):
    compras = Compra.objects.all()
    return render(request, 'carrinho/compra_list.html', {'compras': compras})
