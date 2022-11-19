from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path("blog/", post_blog, name='blogPage'),
]
