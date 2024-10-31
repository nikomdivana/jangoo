from django.shortcuts import render, redirect
from .models import posti
from .forms import PostForm

def home(request):
    posts = posti.objects.all
    return render(request,'home.html',context ={'posts': posts})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'create_post.html',
                  context={'form': PostForm()})
def detail_post(request,pk):
    post = posti.objects.get(id=pk)
    return  render(request, 'detail_post.html',
                   context={"post": post})
def update_post(request, pk):
    post = posti.objects.get(id=pk)
    if request.method == "POST":
            form = PostForm(request.POST)
    print(request.POST)
    if form.is_valid():
            form.save()
            return redirect('home')
#DAVNEBDI!!!!!!!!!!!