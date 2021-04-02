from django.shortcuts import render
from .models import Projects

# Create your views here.


def projects(request):
    """ A view to return all projects """
    projects = Projects.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'projects/projects.html', context)
