from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    banner = models.ImageField(default='fallback.png', blank=True)
    title = models.CharField(max_length=128)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
    