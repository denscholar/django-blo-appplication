from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(default='default/default.jpg', upload_to='post_images')
    slug = models.SlugField(null=False, unique=True)
    date_posted = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f'Post Title - {self.title}'

    def get_absolute_url(self):
        return reverse("posts", kwargs={"slug": self.slug})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    body = models.TextField()
    email = models.EmailField(max_length=254)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_at']

        def __str__(self):
            return f'comment by {self.name} on {self.post.title}'
        