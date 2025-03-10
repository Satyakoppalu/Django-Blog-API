from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title= models.CharField(max_length=200)
    content=models.TextField()
    author=models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.title