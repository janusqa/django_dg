from django.db import models


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

    def __str__(self) -> str:
        return self.title
