from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path("blog/", post_blog, name='blogPage'),
    path("blogdetail/<slug:slug>/", postDetail, name='blogdetail'),
]
