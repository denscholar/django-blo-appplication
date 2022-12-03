from django.db import models
from django.utils import timezone
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=100)
    small_title = models.CharField(max_length=50)
    card_icon = models.ImageField(default='default/default.jpg', upload_to='post_images')
    page_image = models.ImageField(upload_to= 'project_images')
    slug = models.SlugField(null=False, unique=True)
    created = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_title", kwargs={"slug": self.slug})
    