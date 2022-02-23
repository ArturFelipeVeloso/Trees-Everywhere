from unicodedata import name
from django.contrib import admin
from django.urls import path

# Grappelli import
from django.conf.urls import include

# Login View import
from django.contrib.auth.views import LoginView, LogoutView

# Login Forms import
from apps.Accounts.forms import LoginForm

# Django Rest Framework import
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

urlpatterns = [
    # Grappelli URL
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    
    # Trees URL
    path('', include('apps.Trees.urls')),
    
    # logout URL
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # API URL
    path('api-token-auth/', obtain_auth_token),
    
    
    # login URL
    path(
        'login/',
        LoginView.as_view(
            template_name='login.html', authentication_form=LoginForm
        ),
        name='login'
    ),
]
