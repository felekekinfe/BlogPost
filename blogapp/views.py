from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView
from .models import Post

class HomeView(ListView):
    model=Post

    template_name='/home/tor/djproj/blogpost/blogpost/templates/home.html'

class ArticleDetailView(DetailView):
    model=Post
    template_name='/home/tor/djproj/blogpost/blogpost/templates/article_detail.html'

class AddPostView(CreateView):
    model=Post
    template_name='/home/tor/djproj/blogpost/blogpost/templates/addpost.html'
    fields='__all__'
