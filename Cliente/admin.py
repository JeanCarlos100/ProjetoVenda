from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cpf', 'criado_em')
    search_fields = ('nome', 'email', 'cpf')
    list_filter = ('criado_em',)  # Adicione filtros para facilitar a navegação
    ordering = ('criado_em',)  # Adicione ordenação padrão
    list_per_page = 20 