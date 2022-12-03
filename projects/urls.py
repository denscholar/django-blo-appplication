from django.urls import path
from .views import *


urlpatterns = [
   path("projects/", project, name='projects')
]
