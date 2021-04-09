from django.shortcuts import render

# Create your views here.


def blog(request):
    """ A view to return all projects """

    return render(request, 'blog/blog.html')
