from django.shortcuts import render, get_object_or_404
from .models import Post, PostComment
from .forms import CreatePostCommentForm
# Create your views here.


def blog(request):
    """ A view to return all projects """
    blog_post = Post.objects.all()

    context = {
        'blog_post': blog_post
    }
    return render(request, 'blog/blog.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = PostComment.objects.filter(post=post)
    form = CreatePostCommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }

    return render(request, 'blog/post_detail.html', context)
