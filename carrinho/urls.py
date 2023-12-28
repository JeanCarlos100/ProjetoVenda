# carrinho/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('selecionar_produtos/', views.selecionar_produtos, name='selecionar_produtos'),
    path('visualizar_compras/', views.visualizar_compras, name='visualizar_compras'),
]
