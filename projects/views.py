from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required

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

    template = 'projects/project_detail.html'
    context = {
        'project': project,
    }

    return render(request, template, context)


@login_required
def add_project(request):
    """ A view to add new projects """

    if not request.user.is_superuser:
        return redirect(reverse('project'))

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            return redirect(reverse('project_detail', args=[project.slug]))
        else:
            print('Form not valid. It failed')
    else:
        form = PostForm()

    template = 'projects/add_project.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_project(request, slug):
    """ A view to edit a project """
    if not request.user.is_superuser:
        return redirect(reverse('project'))

    project = get_object_or_404(Project, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect(reverse('project_detail', args=[project.slug]))
        else:
            print('Form not valid. It failed')
    else:
        form = PostForm(instance=project)

    template = 'projects/edit_project.html'
    context = {
        'form': form,
        'project': project
    }

    return render(request, template, context)
