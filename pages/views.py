from django.shortcuts import render
from blog.models import Post
from projects.models import Project

def home(request):
    posts = Post.objects.all()[:3]
    projects = Project.objects.all()

    context = {
        "posts": posts,
        "projects":projects,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    context = {}
    return render(request, 'pages/services.html', context)


# def post_detail(request, slug):
#     post_detail = Post.objects.get(slug=slug)
#     context = {
#         "post_detail":post_detail,
#     }
#     return render(request, 'pages/home.html', context)
