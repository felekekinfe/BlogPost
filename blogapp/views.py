from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView
from .models import Post

class HomeView(ListView):
    model=Post

    template_name='home.html'

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_detail.html'

class AddPostView(CreateView):
    model=Post
    template_name='addpost.html'
    fields='__all__'
