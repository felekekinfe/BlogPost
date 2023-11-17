from django.urls import path
from .views import DeletePostView,UpdatePostView,AddPostView,HomeView,ArticleDetailView,like_post

urlpatterns = [
    # path('editprofile/<int:pk>',UpdateProfile.as_view(),name='editprofile'),

    path('',HomeView.as_view(),name='home'),
    path('like/<int:post_id>',like_post,name="like_post"),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article_detail_view'),
    path('addpost/',AddPostView.as_view(),name='addpost'),
    path('update/<int:pk>',UpdatePostView.as_view(),name='updatepost'),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name="deletepage"),

]
