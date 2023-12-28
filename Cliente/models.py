from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True) 
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf or 'N/A'})"
