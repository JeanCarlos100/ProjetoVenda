from django.urls import path
from .views import cadastrar_cliente, editar_cliente, remover_cliente, lista_clientes

urlpatterns = [
    path('cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
    path('editar/<int:cliente_id>/', editar_cliente, name='editar_cliente'),
    path('remover/<int:cliente_id>/', remover_cliente, name='remover_cliente'),
    path('listar/', lista_clientes, name='lista_clientes'),
]
