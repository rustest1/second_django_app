# simp_blog2/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]
