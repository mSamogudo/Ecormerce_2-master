from django import forms


class FormularioDePagamentoForm(forms.Form):
    nome = forms.CharField(max_length=255)
    apelido = forms.CharField(max_length=255)
    email = forms.EmailField()
    telefone = forms.IntegerField()
    bairro = forms.CharField(max_length=255)
    stripe_token = forms.CharField(max_length=255)
