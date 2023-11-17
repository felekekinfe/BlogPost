from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField



class Post(models.Model):
    title=models.CharField(max_length=100)
    header_image=models.ImageField(blank=True,null=True, upload_to='images/')
    title_tag=models.CharField(max_length=100)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=RichTextField()
    post_date=models.DateField(auto_now_add=True)
    catagory=models.CharField(max_length=10,choices=[("tech",'tech'),("soccer",'soccer'),("game",'game'),("movies",'movies')])
    likes=models.ManyToManyField(User,related_name='blog_post')
    unlike=models.ManyToManyField(User,related_name='unlike_user')
    snippets=models.CharField(max_length=255)

    def total_likes(self):
        return self.likes.count()
        
    def total_unlikes(self):
        return self.unlike.count()

    def __str__(self):
        return str(self.author)
    
    def get_absolute_url(self):
        return reverse("home")

""" class Lazy(models.Model):
    nottitle=models.CharField(max_length=100)
    nottitle_tag=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nottitle
    
    def get_absolute_url(self):
        return reverse("home") """
    
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/userprofile/")

    website=models.CharField(max_length=255,null=True,blank=True)
    facebook=models.CharField(max_length=255,null=True,blank=True)
    linkedin=models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return str(self.user)
    


    
