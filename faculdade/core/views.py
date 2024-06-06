from django.urls import reverse
from urllib.parse import urlencode
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Produto, Pedido, Carrinho
from .forms import ProdutoForm
from django.http import HttpResponseNotAllowed

# Create your views here.

def login(request):
    return render(request, 'app/login.html')

def efetuar_login(request):
    if request.method == "POST":
        msg = 'Seja bem vindo ao sistema'
        status = 'success'

        base_url = reverse('lista_produtos')
        query_string =  urlencode({'msg': msg, 'status' : status})

        return redirect(f'{base_url}?{query_string}')
    
    return HttpResponseNotAllowed(['POST'])

def cadastro_pedido(request):
    return render(request, 'app/cliente_cadastro_pedido.html')

def lista_pedidos(request):
    return render(request, 'app/cliente_pedidos.html')

def lista_produtos(request):
    columns = ['Código', 'Nome', 'Custo', 'Valor']
    produtos = Produto.objects.all()


    return render(request, 'app/admin_lista_produtos.html', {
        'produtos': produtos,
        'produtos_columns': columns,
        'logado': True,
        'user_name' : 'P_SANTOS'
    })

def novo_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)

    if form.is_valid():
        form.save()
        msg = 'Produto adicionado com sucesso!'
        status = 'success'
    else:
        msg = 'Erro ao adicionar produto!'
        status = 'error'
        form = ProdutoForm()


    base_url = reverse('lista_produtos')
    query_string =  urlencode({'msg': msg, 'status' : status})
    return redirect(f'{base_url}?{query_string}')

def editar_produto(request, pk):
    produto = get_object_or_404(produto, pk=pk)

    if request.method == "POST":
        form = produtoForm(request.POST, instance=produto)

    if form.is_valid():

        form.save()
        return redirect('lista_produtos')

    else:
        form = produtoForm(instance=produto)

    return render(request, 'templates/form_produto.html', {'form': form})

def deletar_produto(request, pk):
    produto = get_object_or_404(produto, pk=pk)

    if request.method == "POST":
        produto.delete()
        return redirect('lista_produtos')

    return render(request, 'templates/confirmar_delete.html', {'obj': produto})