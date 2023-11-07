from django.shortcuts import render,redirect
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

def like_post(request,post_id):
    if request.method=="POST":
        post=Post.objects.get(pk=post_id)
        if request.user==post.author:
            if Likes.objects.all() is None:
                like=Likes(post=post,like=request.user)
                like.save()
                return render('/home/tor/djproj/blogpost/blogapp/templates/article_detail.html',context={"post":post,'like':like})
      

            if not Likes.objects.filter(like=request.user,post=post):
                like=Likes(like=request.user,post=post)
                like.save()
                return render('/home/tor/djproj/blogpost/blogapp/templates/article_detail.html',context={"post":post,'like':like})
    return redirect('article_detail_view',pk=post_id)


class AddPostView(CreateView):
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


