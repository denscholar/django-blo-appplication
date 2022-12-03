from django.shortcuts import render
from .models import *

def project(request):
    projects = Project.objects.all()
    context = {
        "projects":projects,
    }
    return render(request, 'project_home.html', context)
