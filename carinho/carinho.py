from django.conf import settings

from produtos.models import Produto


class Carinho:
    def __init__(self, request):
        self.session = request.session
        carinho = self.session.get(settings.CART_SESSION_ID)

        if not carinho:
            carinho = self.session[settings.CART_SESSION_ID] = {}

        self.carinho = carinho

    def __iter__(self):
        for p in self.carinho.keys():
            self.carinho[str(p)]['produto'] = Produto.objects.get(pk=p)

        for item in self.carinho.values():
            item['preco_total'] = item['produto'].preco * item['quantidade']

            yield item

    def __len__(self):
        return sum(item['quantidade'] for item in self.carinho.values())

    def add(self, product_id, quantidade=1, actualizar_quantidade=False):
        product_id = str(product_id)

        if product_id not in self.carinho:
            self.carinho[product_id] = {'quantidade': 1, 'id': product_id}

        if actualizar_quantidade:
            self.carinho[product_id]['quantidade'] += int(quantidade)

            if self.carinho[product_id]['quantidade'] == 0:
                self.remove(product_id)
        self.save()

    def remove(self, produto_id):
        if produto_id in self.carinho:
            del self.carinho[produto_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.carinho
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_custo_total(self):
        for p in self.carinho.keys():
            self.carinho[str(p)]['produto'] = Produto.objects.get(pk=p)

        return sum(item['quantidade'] * item['produto'].preco for item in self.carinho.values())
