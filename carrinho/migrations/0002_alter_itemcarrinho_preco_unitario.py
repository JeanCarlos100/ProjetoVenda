# Generated by Django 5.0 on 2023-12-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcarrinho',
            name='preco_unitario',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
