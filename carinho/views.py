from django.contrib import messages
from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from django.contrib import messages
# Create your views here.
from carinho.carinho import Carinho
from .forms import FormularioDePagamentoForm
from compra.utilities import checkout


def detalhes_do_carinho(request):
    carinho = Carinho(request)

    if request.method == 'POST':
        form = FormularioDePagamentoForm(request.POST)
        if form.is_valid():
            stripe.api_key = settings.STRIPE_SECRET_KEY

            stripe_token = form.cleaned_data['stripe_token']

            charge = stripe.Charge.create(
                amount=int(carinho.get_custo_total() * 100),
                currency='USD',
                description='EMSHOP',
                source=stripe_token
            )
            nome = form.cleaned_data['nome']
            apelido = form.cleaned_data['apelido']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            bairro = form.cleaned_data['bairro']

            compra = checkout(request, nome, apelido, email, telefone, bairro, carinho.get_custo_total())
            carinho.clear()
            return redirect('success')
    else:
        form = FormularioDePagamentoForm()

    remover_do_carinho = request.GET.get('remover_do_carinho', '')
    mudar_quantidade = request.GET.get('mudar_quantidade', '')
    quantidade = request.GET.get('quantidade', 0)

    if remover_do_carinho:
        carinho.remove(remover_do_carinho)
        messages.warning(request, 'O Produto Foi Removido do Carinho')
        return redirect('carinho')

    if mudar_quantidade:
        carinho.add(mudar_quantidade, quantidade, True)
        return redirect('carinho')

    return render(request, 'carinho/carinho.html', {'form': form, 'stripe_pub_key': settings.STRIPE_PUB_KEY})


def success(request):
    return render(request, 'loja/checkout.html')