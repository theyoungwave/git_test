from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post


def home(request):
    contents = Post.objects.all()
    return render(request, 'home.html', {"post_list" : contents})

def detail(request, num):
    post = Post.objects.get(id=num)
    return render(request, 'detail.html', {'result' : post})

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/post/' + str(post.id))