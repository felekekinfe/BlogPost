from django.shortcuts import render
from django.views.generic import UpdateView,CreateView,ListView,DetailView,DeleteView
from .models import Post
from .forms import AddPostForm,UpdatePostForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model=Post

    template_name='home.html'
    ordering=['-post_date']

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_detail.html'

class AddPostView(CreateView):
    model=Post
    form_class=AddPostForm
    template_name='addpost.html'
    #fields='__all__'

class UpdatePostView(UpdateView):
    model=Post
    template_name='update_post.html'
    form_class=UpdatePostForm
    #fields=('title','body')

class DeletePostView(DeleteView):
    model=Post
    template_name='deletepost.html'
    success_url=reverse_lazy("home")


