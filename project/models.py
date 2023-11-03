from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Blog(models.Model):
    title = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False, blank=True, default='')
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)


    def average_rating(self):
        ratings = Rating.objects.filter(blog=self)
        average = ratings.aggregate(Avg('rating'))['rating__avg']
        return average or 0

    def increment_views(self):
        self.views += 1
        self.save()

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        super(Rating, self).save(*args, **kwargs)
        self.blog.average_rating()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE) 
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    content = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)