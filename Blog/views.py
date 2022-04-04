import datetime
from time import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from Blog.forms import CreateComment, CreatePostForm
from Blog.models import  Post
from . models import Comment
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.


def registeruser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!. Check out our Email later :)')

            return redirect('login')
    else:
        form = CreateUserForm
    context = {
            
            'form':form,
                        }

    return render(request,'registration/register.html',context)


def loginpage(request):
    if request.user.is_authenticated:

            return redirect('Home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.info(request, 'Username or password is incorrect')

      
    return render(request,'registration/login.html')

def Blog(request):
    posts=Post.objects.all()
     
    return render(request,'blog.html',{'posts':posts})

def post_detail(request, pk):
    comments=Comment.objects.all()
    com = Comment.objects.last()
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CreateComment(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('Home')
    else:
        form = CreateComment()
    return render(request, 'post-detail.html', {'post': post,'comments':comments,'com':com})

def Home(request):
    posts=Post.objects.all()
    latest_post=Post.objects.last()
    context={'posts':posts,'latest_post':latest_post}
 
            
    return render(request,'home.html',context)
    
@login_required(login_url='login')
def Posts(request):
   
    form=CreatePostForm()
    if request.method=='POST':
        form=CreatePostForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return redirect('Home')
        else:
            form = CreatePostForm()

            
    context = {'form':form}

    return render(request,'create-post.html',context)

@login_required(login_url='login')
def add_comment(request, post):
    comments=Comment.objects.all()
    com = Comment.objects.last()
    post = get_object_or_404(Post, post = post,status= 'created')
    if request.method == "POST":
        form = CreateComment(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/' + post.post)
    else:
        form = CreateComment()
    return render(request, 'create_comment.html', {'form': form,'com': com,'comments':comments,'post':post})


def comment_view(request):
    com = Comment.objects.last()
   
    context = {'com': com}
    return render(request, 'postDetail.html', context)

def About(request):
    
    return render(request,'about.html')