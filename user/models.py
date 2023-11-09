from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	bio = models.CharField(max_length=255, blank=True, default='', null=False)
	owner = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/', max_length=1000, null=True)
	resume = models.FileField(upload_to='files/', max_length=1000, null=True)