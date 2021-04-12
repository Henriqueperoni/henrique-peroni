from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

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

    if request.method == 'POST':
        create_comment = PostComment(
            print('Create comment'),
            comment=request.POST.get('comment'),
            user=request.user,
            post=post,
        )
        create_comment.save()

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }

    return render(request, 'blog/post_detail.html', context)


def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('postid'))
        post = get_object_or_404(Post, id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            post.likes_count -= 1
            result = post.likes_count
            post.save()
        else:
            post.likes.add(request.user)
            post.likes_count += 1
            result = post.likes_count
            post.save()

        return JsonResponse({'result': result, })
