from django.db.models import Q
from django.contrib import messages
import random
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddParaCarinhoForm
from .models import Categoria, Produto

from carinho.carinho import Carinho


def procurar(request):
    query = request.GET.get('query', '')
    produtos = Produto.objects.filter(Q(titulo__icontains=query) | Q(descricao__icontains=query))

    return render(request, 'produto/procurar.html', {'produtos': produtos, 'query': query})


def produto_(request, categoria_slug, produto_slug):
    carinho = Carinho(request)

    produto = get_object_or_404(Produto, categoria__slug=categoria_slug, slug=produto_slug)

    if request.method == 'POST':
        form = AddParaCarinhoForm(request.POST)

        if form.is_valid():
            quantidade = form.cleaned_data['quantidade']

            carinho.add(product_id=produto.id, quantidade=quantidade, actualizar_quantidade=False)

            messages.success(request, 'O Produto Foi Adicionado ao Carinho')

            return redirect('produto', categoria_slug=categoria_slug, produto_slug=produto_slug)
    else:
        form = AddParaCarinhoForm()

    produtos_iguais = list(produto.categoria.produtos.exclude(id=produto.id))

    if len(produtos_iguais) >= 4:
        produtos_iguais = random.sample(produtos_iguais, 4)

    context = {
        'form': form,
        'produto': produto,
        'produtos_iguais': produtos_iguais
    }
    return render(request, 'produto/detalhes_do_produto.html', context)

"""def checkout(request, produto_slug):
    produto = get_object_or_404(Produto, slug=produto_slug)
    context = {
        'produto': produto
    }
    return render(request, 'loja/checkout.html', context)"""

def categoria_(request, categoria_slug):
    categoria = get_object_or_404(Categoria, slug=categoria_slug)
    context = {
        'categorias': categoria,
    }
    return render(request, 'produto/categoria.html', context)
