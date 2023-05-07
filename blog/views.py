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
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
         comment_form = CommentForm(request.POST)
         if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)

            # Assign the current post to the comment
            new_comment.post = post

            # Save the comment to the database
            new_comment.save()
            messages.success(request, 'Comment will appear upon approval')
            return redirect('blog:blogdetail')
    else:
        comment_form = CommentForm()
        
    context = {
        'post': post,
        "user": user,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog-detail.html', context)


