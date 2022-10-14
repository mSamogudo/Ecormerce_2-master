from .models import Categoria


def menu_categoria(request):
    categorias = Categoria.objects.all()

    return {'menu_categorias': categorias}
