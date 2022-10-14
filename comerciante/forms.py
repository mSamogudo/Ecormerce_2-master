from django.forms import ModelForm

from produtos.models import Produto, Comerciante


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['categoria', 'imagem', 'titulo', 'descricao', 'preco', 'preco_promocial']


class CadastroComercianteForm(ModelForm):
    class Meta:
        model = Comerciante
        fields = ['nome', 'apelido', 'telefone', 'email']
