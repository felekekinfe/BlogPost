from django.shortcuts import reverse, render,redirect,get_object_or_404
from django.views.generic import UpdateView,CreateView,ListView,DetailView,DeleteView
from .models import Post
from .forms import AddPostForm,UpdatePostForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class HomeView(ListView):
    model=Post

    template_name='home.html'
    ordering=['-post_date']

class ArticleDetailView(DetailView):
    # model=Post
    # template_name='article_detail.html'

    # def get_context_data(self, *args,**kwargs):
    #     post=get_object_or_404(Post,id=self.kwargs['pk'])

    #     no_likes=post.total_likes()

    
       
    #     context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
    #     liked=False
    #     if post.likes.filter(id=self.request.user.id).exists():
    #         liked=True

    #     context["liked"]=liked
    #     context["total_likes"] =no_likes 
        

    #     return context
    model=Post
    template_name="article_detail.html"

    def get_context_data(self,*args,**kwargs):
        post=get_object_or_404(Post,id=self.kwargs["pk"])
        no_likes=post.total_likes()


        liked=False

        if post.likes.filter(id=self.request.user.id).exists():
            liked=True
        
        context=super(ArticleDetailView, self).get_context_data(*args,**kwargs)

        context["liked"]=liked
        context["total_likes"]=no_likes

        return context
        



def like_post(request,post_id):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))

    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True


    return redirect(reverse('article_detail_view',args=[post_id]))

# def unlike_post(request,post_id):
#     post=get_object_or_404(Post,id=request.POST.get("post_id"))
#     post.unlike.add(request.user)
#     return redirect(reverse("article_detail_view",args=[post_id]))


    # if request.method=="POST":
    #     post=Post.objects.get(pk=post_id)
    #     if request.user==post.author:  
    #         if Likes.objects.all() is None:
    #             like=Likes(post=post,like=request.user)
    #             like.save()
    #             return render('/home/tor/djproj/blogpost/blogapp/templates/article_detail.html',context={"post":post,'like':like})
      

    #         if not Likes.objects.filter(like=request.user,post=post):
    #             like=Likes(like=request.user,post=post)
    #             like.save()
    #             return render('/home/tor/djproj/blogpost/blogapp/templates/article_detail.html',context={"post":post,'like':like})
    # return redirect('article_detail_view',pk=post_id)


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


# class UpdateProfile(UpdateView):
#     model=User
#     form_class=UserChangeForm
#     template_name='updateProfile.html'
#     success_url=reverse_lazy("home")
