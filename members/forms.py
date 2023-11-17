from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from blogapp.models import Profile






class SignUpForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password1','password2')


class EditProfilForm(UserChangeForm):
    first_name=forms.CharField(max_length=100),
    last_name=forms.CharField(max_length=100),
    username=forms.CharField(max_length=100),
    email=forms.EmailField(),
    last_login=forms.CharField(max_length=100),
    is_superuser=forms.CharField(max_length=100),
    is_staff=forms.CharField(max_length=100),
    is_active=forms.CharField(max_length=100),
    date_joined=forms.CharField(max_length=100)
    website=forms.CharField(max_length=100)
    
    class Meta:
        model=User
   
        fields=('first_name','last_name','username','email','password','last_login','is_superuser','is_staff','is_active','date_joined',)

# class PasswordEditForm(PasswordChangeForm):

#     class Meta:
#         model=User
#         fields=('old_password','new_password1','new_password2')




class EditProfilePic(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic','bio','website','facebook','linkedin']