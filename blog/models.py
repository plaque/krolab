from django.db import models
from django.utils import timezone

class Category(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
