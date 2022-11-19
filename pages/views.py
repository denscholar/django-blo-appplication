from django.shortcuts import render
from blog.models import Post

def home(request):
    # posts = Post.objects.all().order_by('-date_posted')[:3]
    # services = Services.objects.all()[:4]
    posts = Post.objects.all()[:3]

    context = {
        "posts": posts
    }
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    context = {}
    return render(request, 'pages/services.html', context)



