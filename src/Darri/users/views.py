from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from .forms import BlogForm

def login_user(request):
    if request.method =="POST":
        return redirect("templates:login")


    else:
        form=AuthenticationForm()
    return render(request,"templates/accounts/login.html",{"form":form})

def register_view(request):
    form=UserCreationForm()
    return render(request,'templates/users/register.html',{"form":form})

# Create your views here.
def profile_view(request):
    return render(request,'views/profile.html')
def home_view(request):
    return render(request,'views/home.html')

def chatbot_view(request):
    return render(request,'views/Chatbot.html')

def blog_view(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.save()
            messages.success(request, f"{blog.model} blog has been posted successfully!")
            return redirect('home')
        else:
            messages.error(request, "There were errors in your form. Please correct them.")
    elif request.method=='GET':
        blog_form=BlogForm()
        context= {'blog_form': blog_form}
    return render(request, 'views/blog.html',context )
