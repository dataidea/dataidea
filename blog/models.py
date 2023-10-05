from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Author(models.Model):
    name = models.CharField(max_length=122, default='dataidea')
    email = models.CharField(max_length=122, default='datasideaofficial@gmail.com')
    profile = models.CharField(max_length=122, default='No profile provided')

    def __str__(self):
        return self.name
    
class BlogCategory(models.Model):
    name = models.CharField(max_length=122, default='New category')
    description = models.CharField(max_length=122, default='New category description')
    color = models.CharField(max_length=122, default='purple')

    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    slug = models.CharField(max_length=122, default='New Blog Slug')
    cuid = models.CharField(max_length=122, default='New Cuid')
    title = models.CharField(max_length=122)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(to=BlogCategory, on_delete=models.CASCADE, default=1)
    brief = models.TextField(default='')
    cover_image = models.CharField(max_length=122, default='no image')
    popularity = models.FloatField(default=0)
    date_featured = models.CharField(max_length=122, default='no date', null=True)
    content_markdown = models.TextField(default='')

    def __str__(self):
        return self.title
    
    
class BlogComment(models.Model):
    approved = models.BooleanField(default=False) 
    comment = models.TextField(default='New Comment')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=12)
    blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.comment