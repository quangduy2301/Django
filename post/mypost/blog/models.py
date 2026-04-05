from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(viewname="post-detail", kwargs={"pk": self.pk})
    
# class Comments(models.Model):
#     post = models.ForeignKey(Post, related_name="comments")
#     author = models.ForeignKey(User, on_delete=models.CASCADE)