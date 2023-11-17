
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from members.views import PasswordChangeView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:pk>/password/',PasswordChangeView.as_view(template_name='registration/changepassword.html'),name='password'),
    path('',include('blogapp.urls')),
    path('member/',include('django.contrib.auth.urls')),
    path('member/',include('members.urls')),
   #path('password/',PasswordChangeView.as_view(template_name='registration/changepassword.html')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
