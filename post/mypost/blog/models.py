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

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(verbose_name="Nội dung bình luận")
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.post.title} - {self.author.username}'