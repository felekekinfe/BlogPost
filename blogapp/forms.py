from django import forms
from .models import Post
from django.contrib.auth.models import User

class AddPostForm(forms.ModelForm):
   
    class Meta:
        model=Post
        fields=('title','header_image','title_tag','body','snippets','author')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Username','id':'Username','value':'','type':'hidden'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippets':forms.Textarea(attrs={'class':'form-control'})
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','body','snippets')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippets':forms.Textarea(attrs={'class':'form-control'})
        }

# class UpdateProfileForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=('username','first_name','last_name',)

       