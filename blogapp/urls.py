from django.urls import path
from .views import UpdatePostView,AddPostView,HomeView,ArticleDetailView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article_detail_view'),
    path('addpost/',AddPostView.as_view(),name='addpost'),
    path('update/<int:pk>',UpdatePostView.as_view(),name='updatepost')
]
