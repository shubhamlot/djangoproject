from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from accounts import views as accounts_views


urlpatterns=[


path('register/',accounts_views.register,name='register'),
path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
path('profile/',accounts_views.profile,name='profile'),
path('about/',accounts_views.about,name='About'),
]
