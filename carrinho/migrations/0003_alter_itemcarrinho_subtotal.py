# Generated by Django 5.0 on 2023-12-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0002_alter_itemcarrinho_preco_unitario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcarrinho',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
