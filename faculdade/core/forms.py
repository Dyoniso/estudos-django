from django import forms
from .models import Produto, Pedido

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'custo', 'valor']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente_nome_completo', 'cliente_telefone', 'cliente_email', 'id_produto']