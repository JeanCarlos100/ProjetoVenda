# Generated by Django 5.0 on 2023-12-25 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
