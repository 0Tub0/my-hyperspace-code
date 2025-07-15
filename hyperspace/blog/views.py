
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Blog

def post_list(request):
    posts = Blog.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
