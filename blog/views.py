from django.shortcuts import render
from .models import *

def post_blog(request):
    posts = Post.objects.all()
    context =  {
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)
