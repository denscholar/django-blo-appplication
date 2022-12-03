from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path("", views.home, name='homepage'),
    path("services/", views.services, name='services'),
    path("about/", views.about, name='about'),
]