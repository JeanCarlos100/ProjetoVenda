# carrinho/models.py
from django.db import models
from Cliente.models import Cliente
from produtos.models import Produto
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class ItemCarrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Verifica se o preço unitário já está preenchido
        if not self.preco_unitario:
            # Preenche o preço unitário com o preço atual do produto
            self.preco_unitario = self.produto.preco

        # Calcula o subtotal automaticamente
        self.subtotal = self.quantidade * self.preco_unitario

        super().save(*args, **kwargs)

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    data_compra = models.DateTimeField(default=timezone.now)

@receiver(post_save, sender=ItemCarrinho)
def atualizar_valor_total_compra(sender, instance, **kwargs):
    # Atualiza o valor total da compra quando um item é adicionado ao carrinho
    compra, created = Compra.objects.get_or_create(cliente=instance.cliente)
    compra.valor_total = sum(item.subtotal for item in ItemCarrinho.objects.filter(cliente=instance.cliente))
    compra.save()
