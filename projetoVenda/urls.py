from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('carrinho/', include('carrinho.urls')),
    path('produtos/', include('produtos.urls')),
    path('clientes/', include('Cliente.urls')),
    path('admin/', admin.site.urls),
]
