from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Produto, Pedido, Carrinho
from .forms import ProdutoForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def novo_produto(request):
    if request.method == "POST":
        form = produtoForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    else:
        form = produtoForm()

    return render(request, 'templates/form_produto.html', {'form': form})

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