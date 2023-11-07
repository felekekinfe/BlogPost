from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title=models.CharField(max_length=100)
    title_tag=models.CharField(max_length=100)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    catagory=models.CharField(max_length=10,choices=[("tech",'tech'),("soccer",'soccer'),("game",'game'),("movies",'movies')])
    likes=models.ManyToManyField(User,related_name='blog_post')
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("home")

""" class Lazy(models.Model):
    nottitle=models.CharField(max_length=100)
    nottitle_tag=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nottitle
    
    def get_absolute_url(self):
        return reverse("home") """
    




    
