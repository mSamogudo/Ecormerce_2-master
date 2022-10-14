from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.generic import CreateView, FormView

from .models import Comerciante
from .forms import ProdutoForm, CadastroComercianteForm


class CadastroComercianteView(FormView):
    form_class = CadastroComercianteForm
    template_name = 'comerciante/register2.html'

    def form_valid(self, form):
        form.save(False)
        nome = form.cleaned_data['nome']
        print(nome)


'''def registrar_comerciante(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            comerciante = Comerciante.objects.create(nome=usuario.username, criado_por=usuario)
            messages.success(request, 'Cadastrado com Sucesso.')
            return redirect('comerciante_admin')
        messages.error(request, 'Erro ao Cadastrar-se. Informação Inválida.')
    else:
        formulario = UserCreationForm()
    return render(request, template_name='comerciante/registrar_comerciante.html',
                  context={'registrar': formulario})'''


@login_required
def comerciante_admin(request):
    comerciante = request.user.comerciante
    produtos = comerciante.produtos.all()

    total_produtos_disponiveis = 0
    quantidade_de_produtos = 0
    for produto in produtos:
        total_produtos_disponiveis += produto.preco
        quantidade_de_produtos += 1

    context = {'comerciante': comerciante,
               'produtos': produtos,
               'total_produtos_disponiveis': total_produtos_disponiveis,
               'quantidade_de_produtos': quantidade_de_produtos,
               }
    return render(request, 'comerciante/comerciante_admin.html', context)


@login_required
def add_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.comerciante = request.user.comerciante
            produto.slug = slugify(produto.titulo)
            produto.save()
            messages.success(request, 'Produto Adicionado.')
            return redirect('comerciante_admin')
    else:
        form = ProdutoForm()

    return render(request, 'comerciante/adicionar_produto.html', {'form': form})
