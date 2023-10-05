import requests
import markdown
from . models import Blog
from django.db.models import Q
from . models import BlogComment
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.
# def blogs(request):
#     context = {}
#     return render(request, 'blog/blogs.html')


def updateBlogs(request):
    username = 'jumashafara'
    page = 1
    all_blogs = []

    while True:
        query = """
        query GetAllBlogsByUser($username: String!, $page: Int) {
            user(username: $username) {
                publication {
                    posts (page:  $page){
                        slug
                        cuid
                        title
                        brief
                        coverImage
                        popularity
                        dateFeatured
                        contentMarkdown
                    }
                }
            }
        }
        """
        variables = {
            "username": username,
            "page": page
        }

        response = requests.post(
            "https://api.hashnode.com",
            json={"query": query, "variables": variables},
        )

        data = response.json()['data']['user']['publication']['posts']
        all_blogs.extend(data)

        if len(data) == 0:
            break
        else:
            page += 1

    for blog in all_blogs:
        if not Blog.objects.filter(cuid=blog['cuid']).exists():
            new_blog = Blog(
                slug=blog['slug'],
                cuid=blog['cuid'],
                title=blog['title'],
                brief=blog['brief'],
                cover_image=blog['coverImage'],
                popularity=blog['popularity'],
                date_featured=blog['dateFeatured'],
                content_markdown=blog['contentMarkdown'],
                )
            new_blog.save()
        else:
            update = Blog.objects.get(cuid=blog['cuid'])
            update.title=blog['title']
            update.brief=blog['brief']
            update.cover_image=blog['coverImage']
            update.popularity=blog['popularity']
            update.date_featured=blog['dateFeatured']
            update.content_markdown=blog['contentMarkdown']
            update.save()

    context = {'state': 'success', 'message': 'Updated blogs'}
    template_name = 'components/message.html'
    return render(request=request, template_name=template_name, context=context)


def blogs(request):
    # Fetch Blogs
    blogs = Blog.objects.all()

    # Sort
    sorted_blogs = sorted(blogs, key=lambda k: k.popularity, reverse=True)

    # pagination
    paginator = Paginator(sorted_blogs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'blogs': page_obj}
    template_name = 'blog/blogs.html'
    return render(request=request, template_name=template_name, context=context)


def blogDetails(request):
    # Fetch Blog Details
    try:
        blog = Blog.objects.get(slug=request.GET.get('slug'))
        related = Blog.objects.filter(category=blog.category)
    except Blog.DoesNotExist:
        context = {'state': 'danger', 'message': 'Blog not found'}
        template_name = 'components/message.html'
        return render(request=request, template_name=template_name, context=context)
    # Fetch Blog Comments
    comments = BlogComment.objects.filter(blog=blog)

    
    context = {
        'blog': blog, 
        'details': markdown.markdown(blog.content_markdown), 
        'comments': comments,
        'related': related[:4]
        }
    return render(request, 'blog/blog_details.html', context=context)


# Comments
def comment(request):

    if request.user.is_anonymous:
        user = User.objects.get(id=12)
    else:
        user = request.user

    try:
        comment = BlogComment(
            comment = request.POST.get(key='comment'),
            blog = Blog.objects.get(slug=request.POST.get(key='slug')),
            user = user
        )

        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
        context = {'message': 'An error occured while trying to add your comment', 'state':  'danger'}
        template_name = 'components/message.html'
        return render(request=request, template_name=template_name, context=context)
    

def search(request):
    query = request.POST.get(key='query')
    blogs = Blog.objects.filter(
        Q(title__icontains=query) |
        Q(content_markdown__icontains=query)|
        Q(category_id=query)
    )

     # Sort
    sorted_blogs = sorted(blogs, key=lambda k: k.popularity, reverse=True)

     # pagination
    # paginator = Paginator(sorted_blogs, 4)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {'blogs': sorted_blogs}
    template_name = 'blog/blogs.html'
    return render(request=request, template_name=template_name, context=context)