from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from userfeed.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def user_signin(request):
     if request.method=='POST':
          username=request.POST['username']
          email=request.POST['email']
          password=request.POST['password']
          cpassword=request.POST['cpassword']
          if(password==cpassword):
               user=User.objects.create_user(username,email,password)
               user.save()
               print("Create profile pe jayega")
               u = authenticate(username=username, password=password)
               if u is not None:
                   login(request, u)
               return redirect('/createprofile/')      
          else:
             messages.error(request,"Passwords do not match")
             return render(request,'account/signup.html')
     
     return render(request,'account/signup.html')
def user_login(request):
     if request.method=='POST':
         username=request.POST['username']
         password=request.POST['password']
         user = authenticate(username=username, password=password)
         if user is not None:
           login(request, user)
           messages.success(request,"You are sucessfully logged in")
           print("This is happening")
           return redirect('/userfeed/')
         else:
              messages.error(request,"User does not exist")
              return redirect('/login/')
     return render(request,'account/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('/login/')
def createprofile(request):
          if request.method=='POST':
              dp=request.FILES['dp']
              bio=request.POST['bio']
              user=request.user
              userprof=UserProfile(user=user,dp=dp,bio=bio)
              userprof.save()
              messages.success(request,"Your profile sucessfully saved!")
              return redirect('/userfeed/')
          return render(request,'account/createprofile.html')
def search(request):
    search=request.GET["search"]
    allp= User.objects.filter(username__icontains=search)
    params={'allp': allp}
    print("Called or not")
    return render(request, 'userfeed/searchUser.html', params)    
    

    
