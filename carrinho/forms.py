# carrinho/forms.py
from django import forms
from .models import Produto  # Certifique-se de importar corretamente o modelo Produto
# carrinho/forms.py
from django import forms
from Cliente.models import Cliente  # Certifique-se de importar corretamente o modelo Cliente

class SelecaoClienteForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label=None)


class SelecaoProdutoForm(forms.Form):
    produtos = forms.ModelMultipleChoiceField(
        queryset=Produto.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    quantidade = forms.IntegerField(min_value=1)
