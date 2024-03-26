# simp_blog2/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    return render(request, 'simp_blog2/home.html', {'title': 'Home'})

def blogs(request):
    posts = Post.objects.all()
    return render(request, 'simp_blog2/blogs.html', {'title': 'Blogs', 'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'simp_blog2/blog_detail.html', {'title': post.title, 'post': post})
