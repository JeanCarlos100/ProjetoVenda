from django.urls import path
from .views import adicionar_carrinho, listar_compras

urlpatterns = [
    path('adicionar/', adicionar_carrinho, name='adicionar_carrinho'),
    path('listar/', listar_compras, name='listar_compras'),
]
