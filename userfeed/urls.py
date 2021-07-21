from django.contrib import admin
from django.urls import path
from userfeed import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.userfeed,name='feed'),
    path('addpost/',views.addpost,name='addpost'),
    path('like_dislike', views.likePost, name='like_dislike_post'),
    path('postcomment/<int:id>/',views.postcomment,name='postcomment'),
    path('<int:id>/',views.deletepost,name='deletepost'),
    path('<str:user>/',views.userprofile,name='userprofile'),
    path('about/',views.about,name='about')
   
   
]
