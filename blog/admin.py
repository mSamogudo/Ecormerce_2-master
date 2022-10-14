from re import search
from django.contrib import admin

from blog.models import CategoriaDoPost, Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'slug', 'criado_por', 'criado_aos', 'estado')
    list_fileter = ('titulo', 'categoria', 'slug', 'criado_por', 'criado_aos')
    search_filter = ('titulo', 'categoria', 'slug', 'criado_por', 'criado_aos')
    prepopulated_fields = {'slug': ('titulo',)}



@admin.register(CategoriaDoPost)
class CategoriaDoPostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', )
    search_filter = ('titulo', 'slug', )
    prepopulated_fields = {'slug': ('titulo',)}
