from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add/', views.add_project, name='add_project'),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
]
