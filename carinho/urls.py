from django.urls import path

from . import views

urlpatterns = [
    path('', views.detalhes_do_carinho, name='carinho'),
    path('sucesso/', views.success, name='sucesso'),
]
