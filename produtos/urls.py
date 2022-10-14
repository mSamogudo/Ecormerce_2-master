from django.urls import path

from . import views

urlpatterns = [
    path('procurar/', views.procurar, name='procurar'),
    path('<slug:categoria_slug>/<slug:produto_slug>/', views.produto_, name='produto'),
    path('<slug:categoria_slug>/', views.categoria_, name='categoria'),
    # path('pagar/<slug:produto_slug>/', views.checkout, name='pagar-produto'),
]
