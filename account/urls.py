from django.contrib import admin
from django.urls import path, include
from account import views


urlpatterns = [
    path('', views.user_signin,name='user_signin'),
     path('login/', views.user_login,name='user_login'),
     path('logout/', views.user_logout, name="user_logout"),
     path('createprofile/',views.createprofile,name='createprofile'),
     path('search/', views.search, name='search'),
     
]
