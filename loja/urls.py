from django.urls import path

from . import views

urlpatterns = [
    path('', views.Inicio.as_view(), name='inicio'),
    path('loja/', views.Loja.as_view(), name='loja'),
    path('contacto/', views.contactos, name='contactos'),
]
