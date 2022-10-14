from django.db import models
from produtos.models import Produto
from comerciante.models import Comerciante


# Create your models here.


class Compra(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    bairro = models.CharField(max_length=255)
    criada_aos = models.DateTimeField(auto_now_add=True)
    valor_pago = models.DecimalField(max_digits=8, decimal_places=2)
    comerciantes = models.ManyToManyField(Comerciante, related_name='compras')

    class Meta:
        ordering = ['-criada_aos']

    def __str__(self):
        return self.nome


class ItemDaCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name='items', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='items', on_delete=models.CASCADE)
    comerciante = models.ForeignKey(Comerciante, related_name='items', on_delete=models.CASCADE)
    comerciante_pago = models.BooleanField(default=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return self.id
