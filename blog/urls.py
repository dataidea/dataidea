from . import views
from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path(route='', view=views.blogs, name='blogs'),
    path(route='blogs/', view=views.blogDetails, name='blog_details'),
    path(route='comment/', view=views.comment, name='comment'),
    path(route='search/', view=views.search, name='search'),
    path(route='update-blogs/', view=views.updateBlogs, name='update_blogs'),
    # path(route='hashnode-blogs', view=views.hashnodeBlogs, name='hashnode_blogs'), 
]