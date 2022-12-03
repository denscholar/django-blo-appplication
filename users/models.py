from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=250, null=True, blank=True)
    profile_img = models.ImageField(default='default/default_profile.jpg', upload_to='post_images')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self) -> None:
        super().save()

        img = Image.open(self.profile_img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_img.path)

        
    
