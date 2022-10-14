from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('lista-de-posts/', PostList.as_view(), name='lista_de_posts'),
    path('<slug>/', PostDetail.as_view(), name='detalhes_do_post'),
]
