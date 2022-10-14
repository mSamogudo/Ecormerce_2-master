from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Comerciante(models.Model):
    nome = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, max_length=250, null=False,
                             blank=False)
    apelido = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField()
    telefone = models.IntegerField(null=True, blank=True)
    criado_aos = models.DateTimeField(auto_now_add=True)

    # criado_por = models.OneToOneField(User, related_name='comerciante', on_delete=models.CASCADE)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
