from django.shortcuts import get_object_or_404, render
from django.template import context
from django.views.generic import ListView, DetailView

from blog.models import Post


# Create your views here.

class PostList(ListView):
    model = Post
    context_object_name = 'lista_de_posts'
    template_name = "blog/blog.html"


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/blog-details.html'
