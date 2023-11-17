from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from. forms import SignUpForm,EditProfilForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from blogapp.models import Profile
from .forms import EditProfilePic

# def showprofile(request,pk):
#     userprofile=Profile.objects.filter(id=pk)
#     context={"userprofile":userprofile}

#     return render(request, "registration/user_profile.html", context)

class EditProfilePicView(generic.UpdateView):
    model=Profile
    fields=['user','profile_pic','bio']
    template_name='registration/editprofilepic.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user


class ShowProfileView(generic.DetailView):
    models=Profile
    template_name="registration/user_profile.html"
    

    def get_queryset(self):
        return Profile.objects.filter(id=self.kwargs['pk'])
    
    def get_context_data(self, *args,**kwargs):
        
        #user=get_object_or_404(self.get_queryset(),id=self.kwargs["pk"])
        context = super(ShowProfileView,self).get_context_data()
        context["userprofile"] =self.get_queryset() 
        return context
    




class PasswordChangeView(PasswordChangeView):
    form_class=PasswordChangeForm

    success_url=reverse_lazy('home')

    
 


class UserRegisterView(generic.CreateView):
    form_class=SignUpForm
    template_name='registration/register.html'
    #by default taks 'form' as form object in your templates if u use class based form or the form is created using django Usercreationform
    success_url=reverse_lazy('login')


class EditProfileView(generic.UpdateView):
   
    form_class=EditProfilForm
    template_name='registration/Edit Profile.html'
    #by default taks 'form' as form object in your templates if u use class based form or the form is created using django Usercreationform
    success_url=reverse_lazy('home')

    #get_object method used to pass the current user as parametr for supperclass UpdateViews
    def get_object(self):


        return self.request.user




