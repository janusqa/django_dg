from django.db import models
from django.contrib.auth.models import User


# Create your models here
# https://docs.djangoproject.com/en/5.0/ref/models/fields
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(
        default="fallback.png", blank=True
    )  # blank=True means this field is optional
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.title
