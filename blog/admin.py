from django.contrib import admin
from .models import Blog
from .models import Author
from .models import BlogComment
from .models import BlogCategory

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    filter_horizontal = ['authors']

admin.site.register(model_or_iterable=[Blog, BlogCategory, Author, BlogComment])
