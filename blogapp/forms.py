from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
   
    class Meta:
        model=Post
        fields=('title','title_tag','catagory','author','body')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','body')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }