from django.shortcuts import render, redirect
from .models import Post, UserProfile, Comment, Like
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
import json
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.
def userfeed(request):
    d=Post.objects.all().order_by('-id')
    ru=UserProfile.objects.all()
    data={'post':d, 'rightuser': ru}
    return render(request,'userfeed/feed.html',data)
def addpost(request):
     if request.method=='POST':
         photo=request.FILES['photo']
         caption=request.POST['caption']
         user=request.user
         post=Post(user=user,photo=photo,caption=caption)
         post.save()
         messages.success(request,"Your post added to the feeds!")
         return redirect('/userfeed')
     else:
         return redirect('/userfeed')
def deletepost(request,id):
    post_=Post.objects.filter(id=id)
    post_.delete()
    messages.success(request,"Post deleted!")
    return redirect('/userfeed')

    
def userprofile(request,user):
    userp=User.objects.filter(username=user)
    
    if userp:
     ans=UserProfile.objects.get(user=userp[0])
     uname=ans.user
     bio=ans.bio
     followers=ans.followers
     following=ans.following
     p=Post.objects.filter(user=uname)
     dp=ans.dp
     posts=p

     dic={'user':uname,
     'bio':bio,
     'dp':dp,
     'followers':followers,
     'following':following,
     'p':p}
     
    else:
        return HttpResponse("NO such user!")
    return render(request,'userfeed/userprofile.html',dic)
def postcomment(request, id):
    passc= Comment.objects.filter(post_comment=id)
    if request.method=='POST':
        comment_t=request.POST.get('comment_t')
        comment_user=request.user
        post_comment= Post.objects.get(id=id)
        comment=Comment(comment_text= comment_t,user_comment=comment_user,post_comment=post_comment)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
    return render(request,'userfeed/comment.html',{'passc':passc, "id":id})
def about(request):
    return render(request,'userfeed/about.html')
def likePost(request):
    post_id = request.GET.get("likeId","")
    post = Post.objects.get(id=post_id)
    user = request.user
    like = Like.objects.filter(post=post, user=user)
    liked = False

    if like:
        Like.dislike(post, user)
    else:
        liked = True
        Like.like(post, user)

    resp = {
        'liked': liked
    }
    response = json.dumps(resp)
    print(response)
    return HttpResponse(response, content_type="application/json")

   

        

