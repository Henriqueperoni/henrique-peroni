from django.shortcuts import render, get_object_or_404
from .models import Project
from .forms import PostForm

# Create your views here.


def projects(request):
    """ A view to return all projects """
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'projects/projects.html', context)


def project_detail(request, slug):
    """ A view to show individual project details """
    project = get_object_or_404(Project, slug=slug)

    context = {
        'project': project,
    }

    return render(request, 'projects/project_detail.html', context)


def add_project(request):
    """ A view to add new projects """
    form = PostForm()

    context = {
        'form': form
    }

    return render(request, 'projects/add_project.html', context)
