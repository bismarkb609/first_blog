from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class UserAccount(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200) 
    userName = models.CharField(max_length=100)
    Email = models.EmailField()
    password = models.CharField(max_length=50)
    

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200) 
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
	
	
    def published(self):
        self.published_date = timezone.now()
        self.save()
    
    
    def __str__(self):
        return self.title
