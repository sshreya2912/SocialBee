from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home/home.html')
def about(request):
    return render(request,'home/about.html')
def contact(request):
    if request.method=="POST":
     name=request.POST['name']
     email=request.POST['email']
     phone=request.POST['phone']
     subject=request.POST['subject']
     
     if(len(name)<=2 or len(email)<=5 or len(phone)<10):
       messages.error(request,"Please fill the form correctly")
       contact=Contact(name=name,phone=phone,email=email,subject=subject) 
       contact.save() 
     else:
         messages.success(request,"Your message has been sent!")
           
    return render(request,'home/contact.html')
    