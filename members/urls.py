from django.urls import path
from .views import UserRegisterView,EditProfileView,PasswordChangeView,ShowProfileView,EditProfilePicView


urlpatterns = [
    path('register/', UserRegisterView.as_view(),name='register'),
    path('editprofile/',EditProfileView.as_view(),name='editprofile'),
    path('user_profile/<int:pk>',ShowProfileView.as_view(),name='showprofile'),
    path('edit_user_profile_pic/<int:pk>',EditProfilePicView.as_view(),name='editprofilepic'),
   
    #path('<int:pk>/password/',PasswordChangeView.as_view(template_name='registration/changepassword.html'),name='password'),
    
    

]
