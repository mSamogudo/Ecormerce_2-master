from django.db import models
from django.conf import settings

# Create your models here.
STATUS = ((1, 'Publicado'), (0, 'Rascunho'))


class CategoriaDoPost(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=False, max_length=255)

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=False, max_length=255)
    categoria = models.ForeignKey(CategoriaDoPost, on_delete=models.CASCADE)
    descricao = models.TextField()
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    criado_aos = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='imagens_do_post')
    estado = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-criado_aos']

    def __str__(self):
        return self.titulo
