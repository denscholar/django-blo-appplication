from django.urls import path
from .views import *

app_name = 'projects'

urlpatterns = [
   path("projects/", project, name='projects_list'),
   path("project/<slug:slug>/", project_detail, name='project_detail'),
]
