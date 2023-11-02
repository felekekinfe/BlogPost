from django.shortcuts import render
from django.views.generic import UpdateView,CreateView,ListView,DetailView
from .models import Post
from .forms import PostForm

class HomeView(ListView):
    model=Post

    template_name='home.html'

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_detail.html'

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='addpost.html'
    #fields='__all__'

class UpdatePostView(UpdateView):
    model=Post
    template_name='update_post.html'
    form_class=PostForm
    #fields=('title','body')

