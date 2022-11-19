from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(default='default/default.jpg', upload_to='media/')
    date_posted = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f'Post Title - {self.title}'
    


