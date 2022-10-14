from carinho.carinho import Carinho

from .models import Compra, ItemDaCompra


def checkout(request, nome, apelido, email, telefone, bairro, valor):
    compra = Compra.objects.create(nome=nome, apelido=apelido, email=email, telefone=telefone, bairro=bairro,
                                   valor_pago=valor)

    for item in Carinho(request):
        ItemDaCompra.objects.create(compra=compra, produto=item['produto'], comerciante=item['produto'].comerciante,
                                    preco=item['produto'].preco, quantidade=item['quantidade'])

        compra.comerciantes.add(item['produto'].comerciante)
    return compra
