import random

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from blog.models import Post
from produtos.models import Produto, Categoria


# Create your views here.
class Inicio(TemplateView):
    template_name = 'loja/home.html'

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all().order_by('?')
        context['ultimos_produtos'] = Produto.objects.all().order_by('?')[0:3]
        context['produtos_recentes'] = Produto.objects.all().order_by('-adicionado_aos')[0:3]
        context['produtos_mais_visualisados'] = Produto.objects.all().order_by('-adicionado_aos')[0:3]
        context['ultimos_posts'] = Post.objects.all().order_by('-titulo')[0:4]
        return context

'''def inicio(request):
    novos_produtos = Produto.objects.all()[0:3]
    produtos = Produto.objects.all().order_by('titulo')[0:8]
    ultimos_posts = Post.objects.all().order_by('-criado_aos')[0:4]

    context = {
        'novos_produtos': novos_produtos,
        'produtos': produtos,
        'ultimos_posts': ultimos_posts,
    }
    return render(request, 'loja/home.html', context)'''


class Loja(TemplateView):
    model = Produto
    paginate_by = 8
    template_name = 'loja/loja.html'

    def get_context_data(self, **kwargs):
        context = super(Loja, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all().order_by('?')
        context['ultimos_produtos'] = Produto.objects.all().order_by('?')[0:3]
        context['produtos_recentes'] = Produto.objects.all().order_by('-adicionado_aos')[0:3]
        context['produtos_em_promocao'] = Produto.objects.all().order_by('preco_promocial')
        return context


def ultimos_produtos(request):
    ultimos_produtos = Produto.objects.all().order_by('-titulo')[0:3]
    novos_produtos = Produto.objects.all()[0:3]

    context = {
        'novos_produtos': novos_produtos,
        'ultimos_produtos': ultimos_produtos,
    }
    return render(request, 'loja/ultimos_produtos.html', context)


def contactos(request):
    return render(request, 'loja/contactos.html')
