from django.shortcuts import render, redirect
from .form import CommentForm
from django.contrib import messages
from .models import *

def post_blog(request):
    posts = Post.objects.all()
    context =  {
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)

def postDetail(request, slug):
    post = Post.objects.get(slug=slug)
    user = User.objects.filter(username = 'denscholar').first

    commentForm = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment will appear uipon approval')
            return redirect('blog:blogdetail')
    else:
        form = CommentForm()
        
    context = {
        'post': post,
        "user": user,
        'form': form,
    }

    return render(request, 'blog/blog-detail.html', context)


