from django.db.models import query
from django.forms.widgets import NullBooleanSelect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import Login, Signup,Postform
from .models import Post
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group


from blog import forms

# Create your views here.
def search(request):
     query=request.GET['query']
     posts= Post.objects.filter(title__icontains=query)
     return render(request,'blog/search.html',{'posts':posts})

def home(request):
   posts=Post.objects.all()
   return render(request,'blog/home.html',{'posts':posts})

def user_login(request):
   if not request.user.is_authenticated:
      if request.method == "POST":
         form = Login(request=request,data=request.POST)
         if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user= authenticate(username=uname,password=upass)
            if user is not None :
               login(request,user)
               messages.success(request,'LOGIN SUCCESFULLY !!')
               return HttpResponseRedirect('/dashboard/')
      else :
         form = Login()
      return render(request,'blog/login.html',{'form':form})
   else :
      return HttpResponseRedirect('/dashboard/')
   

def user_logout(request):
   logout(request)
   return render(request,'blog/home.html')

def about(request):
   return render(request,'blog/about.html')


def signup(request):
   if request.method =='POST' :
      form = Signup(request.POST)
      if form.is_valid():
         messages.success(request,'Congratulation')
         user= form.save()
         group = Group.objects.get(name='Author')
         user.groups.add(group)
   else :
      form = Signup()
   return render(request,'blog/signup.html',{'form':form})

def dashboard(request):
      posts = Post.objects.all()   
      if request.user.is_authenticated:
         Uname=request.user.username
         return render(request,'blog/dashboard.html',{'posts':posts,'Uname':Uname})
      else :
          return render(request,'blog/dashboard.html',{'posts':posts})

          
def Addpost(request):
   if request.user.is_authenticated:
      if request.method == "POST":
         form = Postform(request.POST)
         if form.is_valid():
            title=form.cleaned_data['title']
            desc=form.cleaned_data['desc']
            university=form.cleaned_data['university']
            uname=form.cleaned_data['uname']
            pst=Post(title=title,desc=desc,university=university,uname=uname)
            pst.save()
            form = Postform()
            messages.success(request,'Add successfully !!')
      else :
         form = Postform()
      return render(request,'blog/addpost.html',{'form':form})
   else :
       return HttpResponseRedirect('/login/')


def contact(request):
   return render(request,'blog/contact.html')

def Updatepost(request,id):
  if request.user.is_authenticated:
     if request.method == "POST" :
        pi= Post.objects.get(pk=id)
        form = Postform(request.POST,instance=pi)
        if form.is_valid():
           form.save()
           messages.success(request,'Edit successfully !!')
     else :
         pi= Post.objects.get(pk=id)
         form = Postform(instance=pi)
    
     return render(request,'blog/updatepost.html',{'form':form})
  else :
       return HttpResponseRedirect('/login/')

def Deletepost(request,id):
  if request.user.is_authenticated:
     if request.method == "POST" :
        pi= Post.objects.get(pk=id)
        pi.delete()
        messages.success(request,'Delete successfully !!')
     return HttpResponseRedirect('/dashboard/')
  else :
       return HttpResponseRedirect('/login/')
