from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Post(models.Model):
    title_en = models.CharField(max_length=100, null=True, blank=True)
    title_de = models.CharField(max_length=100, null=True, blank=True)
    content_en = HTMLField(blank=True)
    content_de = HTMLField(blank=True)
    photo = models.ImageField(upload_to='cars', null=True, blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return str(self.title_en)
