from django.shortcuts import render
from .models import *

def project(request):
    projects = Project.objects.all()
    context = {
        "projects":projects,
    }
    return render(request, 'projects/projects_list.html', context)

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    context = {
        "project":project,
    }
    return render(request, 'projects/project_details.html', context)
