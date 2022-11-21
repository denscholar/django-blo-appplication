from django.shortcuts import render
from .models import *

def post_blog(request):
    posts = Post.objects.all()
    context =  {
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)

def postDetail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }

    return render(request, 'blog/blog-detail.html', context)
