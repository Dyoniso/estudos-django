from django import forms
from .models import Produto, Pedido, Carrinho

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'custo', 'valor']