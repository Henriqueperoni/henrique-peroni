from django.shortcuts import render

# Create your views here.


def projects(request):
    """ A view to return all projects """
    return render(request, 'projects/projects.html')
