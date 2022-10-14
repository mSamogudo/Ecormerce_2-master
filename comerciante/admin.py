from django.contrib import admin

from .models import Comerciante


@admin.register(Comerciante)
class ComercianteAdmin(admin.ModelAdmin):
    list_filter = ('nome', 'criado_aos')
    list_display = ('nome', 'criado_aos')
    search_fields = ('nome', 'criado_aos')
