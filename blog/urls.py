from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:post_detail>/', views.post_detail, name='post_detail'),
    path('like/', views.like, name='like'),
]
