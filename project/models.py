from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False, blank=True, default='')
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'