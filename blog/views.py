from django.shortcuts import render
from .models import Post
# Create your views here.


def posts(request):
    posts = Post.objects.all()
    lang = request.GET.get('lang', None)
    return render(request, 'posts.html', {'posts': posts, 'lang': lang})


def post_detail(request, slug):
    post = Post.objects.filter(slug=slug).first()
    return render(request, 'post_detail.html', {'post': post})
