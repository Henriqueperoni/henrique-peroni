from django.shortcuts import render, get_object_or_404
from .models import Projects

# Create your views here.


def projects(request):
    """ A view to return all projects """
    projects = Projects.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'projects/projects.html', context)


def project_detail(request, project_id):
    """ A view to show individual project details """
    project = get_object_or_404(Projects, pk=project_id)

    context = {
        'project': project,
    }

    return render(request, 'projects/project_detail.html', context)
