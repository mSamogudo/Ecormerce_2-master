from django.contrib import admin

# Register your models here.
from produtos.models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug',)
    prepopulated_fields = {'slug': ('titulo',)}


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'comerciante', 'adicionado_aos', 'slug',)
    list_filter = ('titulo', 'categoria', 'comerciante', 'slug', 'adicionado_aos',)
    search_fields = ('titulo', 'categoria', 'comerciante', 'slug', 'adicionado_aos',)
