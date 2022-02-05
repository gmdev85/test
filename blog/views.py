from django.shortcuts import render
from .models import Post
# Create your views here.

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def post_detail(request, slug):
    print('dewdwdwe')
    post = Post.objects.filter(slug=slug).first()
    return render(request, 'posts.html', {'post': post})
