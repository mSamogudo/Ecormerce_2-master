from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from stdimage import StdImageField

from comerciante.models import Comerciante


class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    imagem = StdImageField('thumbnail_categoria_produto', upload_to='thumbnails_categoria/',
                           variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    ordenacao = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordenacao']

    def __str__(self):
        return self.titulo


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    comerciante = models.ForeignKey(Comerciante, related_name='produtos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    preco_promocial = models.FloatField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    adicionado_aos = models.DateTimeField(auto_now_add=True)
    imagem = StdImageField('thumbnail_produto', upload_to='thumbnails/',
                           variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    class Meta:
        ordering = ['-adicionado_aos']

    def __str__(self):
        return self.titulo
