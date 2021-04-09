from django.shortcuts import render
from .models import Post
# Create your views here.


def blog(request):
    """ A view to return all projects """
    blog_post = Post.objects.all()

    context = {
        'blog_post': blog_post
    }
    return render(request, 'blog/blog.html', context)
