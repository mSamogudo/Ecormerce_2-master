from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registrar-comerciante/', views.ComercianteCreateView.as_view(), name='registrar_comerciante'),
    path('comerciante-admin/', views.comerciante_admin, name='comerciante_admin'),
    # comerciante adiciona Produto
    path('add-produto/', views.add_produto, name='adicionar_produto'),

    # Sair do Sistema
    path('sair/', auth_views.LogoutView.as_view(), name='sair'),
    # Entrar no Sistema
    path('entrar/', auth_views.LoginView.as_view(template_name='comerciante/entrar.html'), name='entrar'),
]
